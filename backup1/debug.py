import client

c = client.CodeFun(None, None)
err = c.login()
if err is not None: print(err)
else: print("Success")