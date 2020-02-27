import requests
url = 'http://172.17.50.43'
r = requests.get(url)
#print(r.text)
print('Status code:\n******')
print(r.status_code)
print('*****')
h=requests.head(url)
print('Header:\n******')
for line in h.headers:
    print(line,":",h.headers[line])
print('headers.php')
url2 = 'http://httpbin.org/headers'
fake_headers = {'User-Agent': 'Mobile'}
r2 = requests.get(url2,headers=fake_headers)
print(r2.text)