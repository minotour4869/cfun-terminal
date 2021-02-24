import submit, login, status
import argparse, os, sys, subprocess

CONFIG_DIRECTORY = os.path.expanduser("~") + '\\.cfun'

def main(argv):
	if not os.path.isdir(CONFIG_DIRECTORY):
		print("Creating directory for first time use...\n")
		os.mkdir(CONFIG_DIRECTORY)
		os.mkdir(CONFIG_DIRECTORY + "\\configs")
		os.mkdir(CONFIG_DIRECTORY + "\\seasions")
	parser = argparse.ArgumentParser(prog="cfun")
	parser.add_argument("command", help="your command")
	parser.add_argument("-f", "--file", help="location of your file", default="main.cpp")
	parser.add_argument("-pr", "--problem", help="problem you want to submit", default=os.path.basename(os.getcwd()))
	parser.add_argument("-u", "--user", help="Username", default=None)
	args = parser.parse_args()
	if args.command == "login":
		login.login_set()
	elif args.command == "submit":
		submit.submit(args.file, args.problem, False)
	# elif args.command == "status":
		

if __name__ == '__main__':
	main(sys.argv[0:])
	