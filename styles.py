def rank(owner, rank):
    if rank == 'Beginner': return '\033[32m' + owner + '\033[0m'
    elif rank == 'Novice': return '\033[92m' + owner + '\033[0m'
    elif rank == 'Coder': return '\033[34m' + owner + '\033[0m'
    elif rank == 'Expert': return '\033[35m' + owner + '\033[0m'
    elif rank == 'Master': return '\033[33m' + owner + '\033[0m'
    elif rank == 'Hacker': return '\033[31m' + owner + '\033[0m'
    else: return '\033[1m' + owner[0] + '\033[31m' + owner[1:] + '\033[0m'

def status(status):
	if status == 'Accepted': return '\033[32m' + status + '\033[0m'
	elif 'Score ' in status: return '\033[92m' + status + '\033[0m'
	elif status == 'Wrong Answer': return '\033[31m' + status + '\033[0m'
	elif status == 'Compile Error': return '\033[90m' + status + '\033[0m'
	elif status == 'Time Limit Exceeded': return '\033[33m' + status + '\033[0m'
	elif status == 'Memory Limit Exceeded': return '\033[33m' + status + '\033[0m'
	elif status == 'Runtime Error': return '\033[34m' + status + '\033[0m'