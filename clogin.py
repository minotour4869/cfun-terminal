import cclient
import colorama
import getpass
import os
import base64

dir = "C:/User/" + getpass.getuser() + '/.cfun'
success_nof = "[" + "\033[32m" + "SUCESS" + "\033[0m" + "] "
fail_nof = "[" + "\033[31m" + "ERROR" + "\033[0m" + "] "

def login():
	# plogin = input("Login from previous session? [Y/N]")
	# if plogin in ["Y", "y"]:
		# f = open(dir + "/login.tmp", "r")
		# if f is None:
			# print(fail_nof + "Data not found!")
			# exit(-1)
		# username = f.readlines()
		# password = base64.b64decode(f.readlines())
	# else: 
	c = cclient.CodeFun(username = "", password = "")
	username, password = c.login_read()
	c.login()
	if c.vertify_login():
		print(success_nof + "Logged in to " + username)
		return username, password
		# os.mkdir()
		# f = open(dir + "/login.tmp", "r")
		# f.write(username)
		# f.write(base64.b64encode(password))
	else:
		print(fail_nof + "Failed to login.")
		exit(-1)