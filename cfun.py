import argparse, sys
import clogin, csubmit

sopt = "h:lg:"
lopt = ["help", "login"]

def main(argv):
	try:
		for arg in argv:
			if arg in ["login"]:
				clogin.login()
			elif arg in ["submit"]:
				csubmit.submit()
	except:
		print("ERROR .-.")

if __name__ == '__main__':
	main(sys.argv[1:])
	