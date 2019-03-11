import requests
import pprint
pp = pprint.PrettyPrinter(indent=2)
r = requests.get('https://api.github.com/events')
pp.pprint(r.json())