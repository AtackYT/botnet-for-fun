import requests

u='https://www.google.com'

while 1 < 10:
    r=requests.get(u)
    print('response', r.status_code)
