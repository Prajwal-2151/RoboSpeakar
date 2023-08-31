import win32com.client as wincom
import requests
import json

speak = wincom.Dispatch("SAPI.SpVoice")
city = input("Enter City\n")

url = f"http://api.weatherapi.com/v1/current.json?key=fa6d913770d646d69a0122731232903&q={city}&aqi=yes"

r = requests.get(url)

dic1 = json.loads(r.text)
t = (dic1["current"]["temp_c"])
dic2 = json.loads(r.text)
d = (dic2["current"]["is_day"])
if d == 1:
    print(f"Temperature of {city} at Day is {t}")
    speak.Speak(f"Temperature of {city} at Day is {t}")
else:
    print(f"Temperature of {city} at Night is {t}")
    speak.Speak(f"Temperature of {city} at Night is {t}")

