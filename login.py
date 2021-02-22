import sys, getpass, os
from client import CodeFun as client
import err

def login_set(username=None):
	os.system('color')
	if username is None:
		username = input("Username: ")
	password = getpass.getpass("Password (Hidden): ")
	
	c = client(username, password)
	error = c.login()
	if error is None:
		print(err.SUCCESS + "Logged to " + c.username)
	else: print(err.ERROR + error)
	c.client.quit()