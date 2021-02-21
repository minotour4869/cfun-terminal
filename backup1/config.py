default_prefix = "main"
default_lang = "C++"

def get_default_file():
	if default_lang == "C++": return default_prefix + ".cpp"
	elif default_lang == "Pascal": return default_prefix + ".pas"
	elif default_lang == "Java": return default_prefix + ".java"
	elif default_lang in ["Python 2", "Python 3"]: return default_prefix + ".py"
	elif default_lang == "Go": return default_prefix + ".go"
	