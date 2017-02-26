import requests

params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
url = "http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi"
r = requests.post(url, data=params)
print(r.text)
