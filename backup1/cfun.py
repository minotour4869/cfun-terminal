import argparse, sys, os
import config
from login import login
from submit import submit

def main(argv):
	parser = argparse.ArgumentParser(prog="cfun")
	parser.add_argument("command", help="command go here")
	parser.add_argument("-p", "--path", help="file path to submit", required=False, default=config.get_default_file())
	parser.add_argument("-pr", "--prob", help="problem you want to submit", required=False, default=os.path.basename(os.getcwd()))
	parser.add_argument("-r", "--relogin", type=bool, help="relogin to site", required=False, default=False)
	args = parser.parse_args()
	
	if args.command == "login":
		login()
	elif args.command == "submit":
		submit(args.path, args.prob, args.relogin)

if __name__ == '__main__':
	main(sys.argv[0:])
	