from client import CodeFun as client
import err, str, login
import os

def style(status):
	if status == 'Accepted': return '\033[32m' + status + '\033[0m'
	elif 'Score ' in status: return '\033[92m' + status + '\033[0m'
	elif status == 'Wrong Answer': return '\033[31m' + status + '\033[0m'
	elif status == 'Compile Error': return '\033[90m' + status + '\033[0m'
	elif status == 'Time Limit Exceeded': return '\033[33m' + status + '\033[0m'
	elif status == 'Memory Limit Exceeded': return '\033[33m' + status + '\033[0m'
	elif status == 'Runtime Error': return '\033[34m' + status + '\033[0m'

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
		print("\tProblem: " + c.prob)
		print("\tUser: " + c.username)
		print("\tLanguage: " + c.sublang)
		print("\tSubmit time: " + c.subtime)
		print("\tStatus: " + style(c.substatus))
		print("\tRunning time: " + c.subruntime)
	c.client.quit()