from client import CodeFun as client

PROFILE_URL = "https://codefun.vn/profile/"

ranklist = ['Newbie', 'Novice', 'Coder', 'Expert', 'Master', 'Hacker', 'Grandmaster']

c = client(None, None)
c.login(True)
c.client.get(PROFILE_URL + c.username)
s = c.client.find_elements_by_xpath('//span')
for item in s:
    ele = item.get_attribute('title').split()
    if ele and ele[0] in ranklist:
        for p in ele:
            if p == ele[0]: c.rank = p
            else: c.owner += p + ' '
        break
print(c.rank + ' ' + c.owner)