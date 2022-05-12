import requests
import json

params = {
  'models': 'nudity,wad',
  'api_user': '{1101636910}',
  'api_secret': '{nqapUNqQvxQn5pgCLG3s}'
}
files = {'media': open('/media/image/', 'rb')}
r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)
output = json.loads(r.text)