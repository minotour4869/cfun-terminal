import submit
# from config import config
import argparse, os, sys, subprocess

def main(argv):
	parser = argparse.ArgumentParser(prog="cfun")
	parser.add_argument("command", help="your command")
	parser.add_argument("-f", "--file", help="location of your file", default="main.cpp")
	parser.add_argument("-pr", "--problem", help="problem you want to submit", default=os.path.basename(os.getcwd()))
	args = parser.parse_args()
	# if args.command == "config":
		# config()
	if args.command == "submit":
		submit.submit(args.file, args.problem, False)

if __name__ == '__main__':
	main(sys.argv[0:])
	