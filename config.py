import os, sys
import cmd_configs
from colorama import Fore as color
from commands.tools import err

def config():
	os.system('color')
	sel = int(input("Config selection: "))
	if sel == 1:
		login.login_set()