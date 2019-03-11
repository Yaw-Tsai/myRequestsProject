import requests
import pprint
pp = pprint.PrettyPrinter(indent=2)
r = requests.get('https://api.github.com/user', auth=('connel.chen@gmail.com', 'github123'))

#Passing Parameters 
payload = {"key1":"value1","key2":"value2"}
r = requests.get('https://httpbin.org/get', params=payload)
pp.pprint(r.url)



'''
print(r.status_code,"\n")
print(r.headers['content-type'], "\n")
print(r.encoding, "\n")
pp.pprint(r.text)
print("\n")
pp.pprint(r.json())
'''