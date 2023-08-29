import requests
import json
city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=48b3a17f78de4129aca110731232908&q={city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
print(wdic["current"]["temp_f"])
