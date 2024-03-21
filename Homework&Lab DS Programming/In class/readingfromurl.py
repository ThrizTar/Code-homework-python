import json
from urllib.request import urlopen

def read_web_page(url):
    assert url.startswith("https://")
    with urlopen(url) as res:
        return res.read()

url = "https: // api.open-meteo.com/v1/forecast?latitude = 37.5139 & longitude = 126.9828&hourly = temperature_2m"

# store the response of URL
response = read_web_page(url)
# storing the JSON response
data_json = json.loads(response)
print('time =', data_json['hourly']['time'][0], end='')
print('\ttemp =',
      data_json['hourly']['temperature_2m'][0], end='')
