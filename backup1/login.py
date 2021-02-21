import client

def login():
	c = client.CodeFun(username = None, password = None)
	err = c.login_set()
	if err is not None: print(err)
	else: print("Success logged to " + c.username)