from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import getpass, base64, os, sys, time, clipboard, re
import err, str

LOGIN_URL = "https://codefun.vn/"
SUBMIT_URL = "https://codefun.vn/submit/"
PROBLEM_URL = "https://codefun.vn/problems/"
PROFILE_URL = "https://codefun.vn/profile/"

CONFIG_DIRECTORY = os.path.expanduser("~") + '\\.cfun'

ranklist = ['Newbie', 'Novice', 'Coder', 'Expert', 'Master', 'Hacker', 'Grandmaster']

class CodeFun:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.lastsub = None
		self.substatus = None
		self.subruntime = None
		self.subtime = None
		self.submemory = None
		self.prob = None
		self.sublang = None
		self.owner = ''
		self.group = None
		self.score = None
		self.ranking = None
		self.rank = ''
		self.acc = None
		self.atc = None
		
		opt = Options()
		# opt.add_argument("--headless")
		opt.add_argument("--log-level=3")
		self.client = Chrome(options=opt)
		self.client.minimize_window()
	
	def get_saved_info(self, incpass=True):
		username = None
		password = None
		# print("ok")
		info_dir = os.path.join(CONFIG_DIRECTORY + '\\seasions', "info")
		if os.path.isfile(info_dir):
			info = open(info_dir, "r")
			data = info.read().rstrip('\n').split()
			username = str.decode(data[0])
			password = str.decode(data[1])
			info.close()
		# print("ok")
		self.username = username
		if incpass: self.password = password
	
	def login(self, get_saved_info=False):
		# Input user information
		if get_saved_info: self.get_saved_info(True)
		if self.username == None:
			return err.NL
		# print("get info with")
		# print(self.username)
		# print(self.password)
		
		# Login via selenium
		self.client.get(LOGIN_URL)
		
		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_xpath('//*[@class="panel-heading"]')
				break
			except: pass
		
		try:
			user_field = self.client.find_element_by_xpath('//*[@placeholder="Username"]')
			user_field.send_keys(self.username)
			pass_field = self.client.find_element_by_xpath('//*[@placeholder="Password"]')
			pass_field.send_keys(self.password)
			submit = self.client.find_element_by_xpath('//*[@type="submit"]')
			submit.click()
		except:
			self.client.quit()
			return err.WF

		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_xpath('//*[@class="panel-heading"]')
				break
			except: pass
			
		time.sleep(1)
		
		# Check for success
		# try:
			# self.client.find_element_by_xpath('//*[@class="alert alert-danger"]')
			# self.client.quit()
			# return err.LC
		# except:x
			# if not get_saved_info:
				# info_dir = os.path.join(CONFIG_DIRECTORY + '\\seasions', "info")
				# info = open(info_dir, "w")
				# euser = str.encode(self.username)
				# epass = str.encode(self.password)
				# info.write(euser + ' ' + epass)
				# info.close()
		
		try:
			t = self.client.find_element_by_xpath('//*[@class="list-group"]')
			if not get_saved_info:
				info_dir = os.path.join(CONFIG_DIRECTORY + '\\seasions', "info")
				info = open(info_dir, "w")
				euser = str.encode(self.username)
				epass = str.encode(self.password)
				info.write(euser + ' ' + epass)
				info.close()
			self.client.get(PROFILE_URL + self.username)
			time.sleep(1)
			cnt = 0
			status_span = self.client.find_elements_by_xpath('//span')
			for item in status_span:
				ele = item.get_attribute('title').split()
				if ele and ele[0] in ranklist:
					for p in ele:
						if p == ele[0]: self.rank = p
						else: self.owner += p + ' '
					break
		except:
			return err.LC
		# print("ok")
			
	def checkprob(self, prob):
		# Check problem is valid or not, by finding its page
		self.client.get(PROBLEM_URL + prob)
		
		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_xpath('//*[@class="panel panel-primary"]')
				break
			except: pass
			
		try:
			self.client.find_element_by_tag_name("code")
			return False
		except:
			return True
			
	def checkfile(self, file):
		ext = file[file.find('.'):]
		if ext in [".cpp", ".pas", ".java", ".py", ".go"]: return True
		return False
		
	def lang(self, file):
		ext = file[file.find('.'):]
		if ext == ".cpp": return "C++"
		elif ext == ".pas": return "Pascal"
		elif ext == ".java": return "Java"
		elif ext == ".py" or ext == ".pypy":
			ver = input("Python ver: ")
			return "Python " + ver
		elif ext == ".go": return "Go"
		
	def submit(self, file_path, prob):
		self.prob = prob
		self.sublang = self.lang(file_path)
		
		# Navigating to the submit page
		self.client.get(SUBMIT_URL)
		
		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_xpath('//*[@class="panel panel-primary"]')
				break
			except: pass
		# print("ok")
			
		# Prepare
		ace_prob = self.client.find_element_by_xpath('//*[@placeholder="Pxxxxx"]')
		ace_prob.send_keys(prob)
		ace_lang = Select(self.client.find_element_by_tag_name("select"))
		ace_lang.select_by_visible_text(self.sublang)
		ace_content = self.client.find_element_by_xpath('//*[@class="ace_text-input"]')
		ace_submit = self.client.find_element_by_xpath('//*[@type="submit"]')
		
		self.client.maximize_window()
		with open(file_path, 'r') as file:
				subs = clipboard.copy(file.read())
				act = ActionChains(self.client)
				
				# Click to the field, Ctrl + V, yea, u know .-.
				act.click(ace_content)
				act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)
				act.click(ace_submit)
				
				act.perform()
		self.client.minimize_window()
		
		time.sleep(1)
		
		# Check cooldown
		try:
			self.client.find_element_by_xpath('//*[@role="alert"]')
			self.client.quit()
			return err.SCD
		except: pass
		
		# Submit
		print("Submiting problem " + prob + " with user " + self.username + "...")
		# print("ok")
		
		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_xpath('//*[@class="col-md-4"]')
				break
			except: pass
		
		#Judge and get result	
		print("")
		while True:
			try:
				self.client.find_element_by_xpath('//span[@class="submission-running"]')
				continue
			except: break
			
		time.sleep(1)
		
		for sub in re.findall(r'\d+', self.client.current_url): self.lastsub = sub
		status_span = self.client.find_elements_by_xpath('//span')
		for item in status_span:
			if "submission-" in item.get_attribute('class'):
				self.substatus = item.get_attribute('innerHTML')
				break
		info = self.client.find_elements_by_xpath('.//b')
		cnt = 0
		for item in info:
			if cnt == 2: self.subruntime = item.get_attribute('innerHTML')
			elif cnt == 3: self.subtime = item.get_attribute('innerHTML')
			elif cnt >= 4: break
			cnt += 1
		
	def get_status(self, username):
		self.client.get(PROFILE_URL + username)
		time.sleep(1)
		
		info = list()
		
		s = self.client.find_elements_by_xpath('//li[@class="list-group-item"]')
		for i in s: info.append(i.find_element_by_xpath('b').get_attribute('innerHTML'))
		self.owner, self.group, self.score, self.ranking = info
		
		table = self.client.find_elements_by_xpath('//table[@class="table table-striped"]')
		info = list()
		
		for i in table:
			cnt = 0
			for ele in i.find_elements_by_xpath('tbody/tr'): cnt+=1
			info.append(cnt)
		
		self.acc, self.atc = info