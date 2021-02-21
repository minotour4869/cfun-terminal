import client, err
import os

def submit(file_path, prob, relogin=False):
	c = client.CodeFun(username = None, password = None)
	
	if not c.checkprob(prob):
		print(err.IP)
		return
	# print("1")
	
	if not os.path.isfile(file_path) or not c.checkfile(file_path):
		print(err.IF)
		return
	# print("1")
		
	status, error = c.submit(file_path, prob, file_path[file_path.find('.'):], relogin)
	if error is not None:
		print(error)
		return
	else:
		print("Judging complete!")
		print("Status: " + status)
	