from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import getpass
import sys
import time
import clipboard

LOGIN_URL = "https://codefun.vn/"
SUBMIT_URL = "https://codefun.vn/submit/"
PROBLEM_URL = "https://codefun.vn/problems/"

class CodeFun:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
		opt = Options()
		opt.add_argument("--headless")
		self.client = webdriver.Chrome(options=opt)
	
	def login_read(self):
		username = input("Username: ")
		self.username = username
		password = getpass.getpass()
		self.password = password
		print("Logging in, please stand still...")
		return username, password
		
	def login(self):
		self.client.get(LOGIN_URL)
		
		browser_handle = self.client.find_element_by_xpath('//*[@placeholder="Username"]')
		browser_password = self.client.find_element_by_xpath('//*[@placeholder="Password"]')
		browser_submit = self.client.find_element_by_xpath('//*[@type="submit"]')
    
		browser_handle.send_keys(self.username)
		browser_password.send_keys(self.password)
		browser_submit.click()
		
	def vertify_login(self):
		while 1:
			try:
				self.client.find_element_by_xpath('//*[@class="panel panel-primary"]')
				break
			except:
				pass
	
		try:
			self.client.find_element_by_xpath('//*[@role="alert"]')
			return False
		except:
			return True

	def checkprob(self, prob):
		self.client.get(PROBLEM_URL + prob)
		# Wait for the page to load..
		while 1:
			try:
				self.client.find_element_by_xpath('//*[@class="col-md-3"]')
				# self.client.find_element_by_tag_name("code")
				break
			except:
				continue
		time.sleep(1)

		try:
			self.client.find_element_by_tag_name("code")
			return False
		except:
			return True
			
	def checklang(self, lang2):
		if lang2 in [".cpp", ".pas", ".java", ".py", ".go"]: return True
		return False
		
	def lang(self, ext):
		if ext == ".cpp": return "C++"
		elif ext == ".pas": return "Pascal"
		elif ext == ".java": return "Java"
		elif ext == ".py" or ext == ".pypy":
			ver = input("Python ver: ")
			return "Python " + ver
		elif ext == ".go": return "Go"
			
	def submit(self, file_path, prob, lang):
		print("ok desu")
		self.client.get(SUBMIT_URL)
		# Wait for the page to be loaded.

		try:
			ace_prob = self.client.find_element_by_xpath('//*[@placeholder="Pxxxxx"]')
			ace_prob.send_key(self.prob)
			ace_lang = Select(self.client.find_element_by_tag_name("select"))
			ace_lang.select_by_visible_text(self.lang)
			ace_content = self.client.find_element_by_xpath('//*[@class="ace_text-input"]')
			ace_submit = browser_submit = self.client.find_element_by_xpath('//*[@type="submit"]')
			
			with open(file_path, 'r') as file:
				subs = clipboard.copy(file.read())
				act = ActionChains(self.client())
				
				# Click to the field, Ctrl + V, yea, u know .-.
				act.click(browser_code_area)
				act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)
				act.click(browser_code_submit_button)
				
				act.perform()
				
			print("Submiting problem " + ace_prob + " with user " + self.username + "...")
			
			problemTitle=self.client.title
			# while problemTitle == 'Submit - Codefun.VN': problemTitle=self.client.title
			currentURL=self.client.current_url
			while currentURL == 'https://codefun.vn/submit/': currentURL=self.client.current_url
			
			while 1:
				try:
					print("Judging...",end='\r')
					self.client.find_element_by_xpath('//*[@class="submission-running"]')
				except:
					print("Judge completed.",end='\n')
					print("Judge Status: " + self.client.find_element_by_xpath('//*[@class="submission-*"]'))
					break
		except:
			print("not ok desu")
			return False
