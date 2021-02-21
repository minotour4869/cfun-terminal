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

LOGIN_URL = "https://codefun.vn/"
SUBMIT_URL = "https://codefun.vn/submit/"
PROBLEM_URL = "https://codefun.vn/problems/"

class CodeFun:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
		opt = Options()
		opt.add_argument("--headless")
		self.client = Chrome(options=opt)
	
	def get_saved_info(incpass):
		username, password = None
		info_dir = os.path.join(os.path.dirname(__file__), "secret")
		if os.path.isfile(info_dir):
			info = open(info_dir, "r")
			data = info.read().rstrip('\n').split()
			username, password = base64.b64decode(data[0:])
		return (username, password if incpass else username)
	
	def login_set(self, username=None):
		# Input user information
		if username is None or self.username is None:
			self.username = input("Username: ")
		else:
			self.username = username
		self.password = getpass.getpass("Password (Hidden): ")
		
		# Login via selenium
		self.client.open(LOGIN_URL)
		
		try:
			user_field = self.client.find_element_by_xpath('//*[@placeholder="Username"]')
			pass_field = self.client.find_element_by_xpath('//*[@placeholder="Password"]')
			submit = self.client.find_element_by_xpath('//*[@type="Submit"]')
		except Exception as err:
			print("Failed to connect site\n" + err)
			self.client.close()
			return
		
		user_field.send_keys(self.username)
		pass_field.send_keys(password)
		submit.click()
		
		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_class_name('panel panel-primary')
				break
			except: pass
		
		# Check for success
		try:
			self.client.find_element_by_xpath('//*[@role="Alert"]')
			print("Invalid credentials")
			self.client.close()
			return
		except:
			info_dir = os.path.join(os.path.dirname(__file__), "secret")
			info = open(info_dir, "w")
			info.write(base64.b64encode(username) + ' ' + base64.b64encode(password))
			info.close()
			print("Success logged to " + username)
			
	def login(self):
		# Input user information
		self.username, self.password = self.get_saved_info(True)
		
		# Login via selenium
		self.client.open(LOGIN_URL)
		
		try:
			user_field = self.client.find_element_by_xpath('//*[@placeholder="Username"]')
			pass_field = self.client.find_element_by_xpath('//*[@placeholder="Password"]')
			submit = self.client.find_element_by_xpath('//*[@type="Submit"]')
		except Exception as err:
			print("Failed to connect site\n" + err)
			self.client.close()
			return
		
		user_field.send_keys(self.username)
		pass_field.send_keys(password)
		submit.click()
		
		# Wait for server respond
		while True:
			try:
				self.client.find_element_by_class_name('panel panel-primary')
				break
			except: pass
		
		# Check for success
		try:
			self.client.find_element_by_xpath('//*[@role="Alert"]')
			print("Login corrupted.")
			self.client.close()
			return
		except:
			pass
