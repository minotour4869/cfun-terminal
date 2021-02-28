from client import CodeFun as client
import err, styles, login
import os

def status(username=None, relogin=False):
	os.system('color')
	if relogin: login.login_set()
	c = client(None, None)
	error = c.login(True)
	if error is not None:
		print(err.ERROR + error)
		
	if username is None: username = c.username
	print("Getting infomation for user " + username + "...")
	c.get_status(username)
	
	print()
	print("\t               Name: " + styles.rank(c.owner, c.rank))
	print("\t              Group: " + c.group)
	print("\t              Score: " + c.score)
	print("\t            Ranking: " + c.ranking)
	print()
	print("\t    Solved problems: " + str(c.acc))
	print("\t Attempted problems: " + str(c.atc))
	c.client.quit()