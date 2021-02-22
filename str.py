import base64

def decode(b64s):
	str_b = base64.b64decode(b64s.encode("ascii"))
	return str_b.decode("ascii")

def encode(str):
	b64_b = base64.b64encode(str.encode("ascii"))
	return b64_b.decode("ascii")