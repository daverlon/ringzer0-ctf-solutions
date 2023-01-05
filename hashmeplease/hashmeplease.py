import requests

# ctf challenge
# https://ringzer0ctf.com/challenges/13

# get msg

r = requests.get('http://challenges.ringzer0team.com:10013/')
s = str(r.content)


start = 'BEGIN MESSAGE -----<br />'
end   = '----- END MESSAGE'
msg = s[s.find(start):s.find(end)]

#msg = msg[s.find('##
gl = 8
start = ' ' * gl
msg = msg[msg.find(start)+gl:]
msg = msg[:msg.find('<br')]
print(msg)

# hash msg

hashurl = 'https://api.hashify.net/hash/sha512/hex?value=' + msg
print(hashurl)

hashed = requests.get(hashurl)
hashed = hashed.json()['Digest']
print(hashed)

r = requests.get('http://challenges.ringzer0team.com:10013/?r=' + hashed)

                       
print(r.content)
