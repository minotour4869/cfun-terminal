import clogin, cclient
import os

def submit():
	username, password = clogin.login()
	c = cclient.CodeFun(username, password)
	c.login()
	probl = input("Problem code: ")
	if not c.checkprob(probl):
		print("Problem not found!")
		exit(-1)
	file_path = input("File path: ")
	file_ext = file_path[file_path.find('.'):]
	if not c.checklang(file_ext) or file_path is None or not os.path.isfile(file_path):
		print("Invalid file!")
		exit(-1)
	print("ok desu")
	c.submit(file_path, probl, c.lang(file_ext))