from client import CodeFun as client
import err, str, login, styles
import os

def submit(file_path, prob, relogin=False):
	os.system('color')
	
	if relogin: login.login_set()
	c = client(None, None)
	error = c.login(True)
	if error is not None:
		print(err.ERROR + error)
		return
	
	if not c.checkprob(prob):
		print(err.ERROR + err.IP)
		return
	
	if not os.path.isfile(file_path) or not c.checkfile(file_path):
		print(err.ERROR + err.IF)
		return
		
	error = c.submit(file_path, prob)
	if error is not None:
		print(err.ERROR + error)
		return
	else:
		print(err.SUCCESS + "Judging completed for submission " + c.lastsub + "!\n")
		print("\t     Problem: " + c.prob)
		print("\t       Owner: " + styles.rank(c.owner, c.rank))
		print("\t    Language: " + c.sublang)
		print("\t Submit time: " + c.subtime)
		print("\t      Status: " + styles.status(c.substatus))
		print("\tRunning time: " + c.subruntime)
	c.client.quit()