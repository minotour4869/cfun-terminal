from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import getpass
import base64
import os
import sys
import time
import clipboard
import err, str

LOGIN_URL = "https://codefun.vn/"
SUBMIT_URL = "https://codefun.vn/submit/"
PROBLEM_URL = "https://codefun.vn/problems/"

class CodeFun:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
		opt = Options()
		# opt.add_argument("--headless")
		self.client = Chrome(options=opt)
	
	def get_saved_info(self, incpass=True):
		username = None
		password = None
		# print("ok")
		info_dir = os.path.join(os.path.dirname(__file__), "secret")
		if os.path.isfile(info_dir):
			info = open(info_dir, "r")
			data = info.read().rstrip('\n').split()
			username = str.decode(data[0])
			password = str.decode(data[1])
		# print("ok")
		self.username = username
		if incpass: self.password = password
	
	def login_set(self, username=None):
		# Input user information
		if username is None or self.username is None:
			self.username = input("Username: ")
		else:
			self.username = username
		self.password = getpass.getpass("Password (Hidden): ")
		
		# Login via selenium
		self.client.get(LOGIN_URL)
		
		try:
			user_field = self.client.find_element_by_xpath('//*[@placeholder="Username"]')
			pass_field = self.client.find_element_by_xpath('//*[@placeholder="Password"]')
			submit = self.client.find_element_by_xpath('//*[@type="submit"]')
		except:
			self.client.quit()
			return err.WF
		
		user_field.send_keys(self.username)
		pass_field.send_keys(self.password)
		submit.click()
		
		print("Logging in to user " + self.username + "...")
		
		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_xpath('//*[@class="panel panel-primary"]')
				break
			except: pass
		
		# Check for success
		try:
			self.client.find_element_by_xpath('//*[@role="alert"]')
			self.client.close()
			return err.IC
		except:
			info_dir = os.path.join(os.path.dirname(__file__), "secret")
			info = open(info_dir, "w")
			euser = str.encode(self.username)
			epass = str.encode(self.password)
			info.write(euser + ' ' + epass)
			info.close()
			return
			
	def login(self):
		# Input user information
		self.get_saved_info(True)
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
		
		# Check for success
		try:
			self.client.find_element_by_xpath('//*[@role="Alert"]')
			self.client.quit()
			return err.LC
		except:
			pass
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
		
	def lang(self, ext):
		if ext == ".cpp": return "C++"
		elif ext == ".pas": return "Pascal"
		elif ext == ".java": return "Java"
		elif ext == ".py" or ext == ".pypy":
			ver = input("Python ver: ")
			return "Python " + ver
		elif ext == ".go": return "Go"
		
	def submit(self, file_path, prob, lang, relogin=False):
		# Login
		if relogin:
			error = self.login_set()
			if error is not None: return None, error
		else:
			error = self.login()
			if error is not None: return None, error
		# print("ok")
		
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
		ace_prob.send_key(prob)
		ace_lang = Select(self.client.find_element_by_tag_name("select"))
		ace_lang.select_by_visible_text(lang)
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
		print("Judging...")
		while True:
			try:
				self.client.find_element_by_xpath('//span[@class="submission-running"]')
				continue
			except: break
		
		status_span = self.client.find_element_by_xpath('//span[@class="submission-*"]')
		status = status_span.get_attribute('innerHTML')
		# print("ok")
		return status.strip(), None