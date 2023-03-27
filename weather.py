import pyttsx3
import requests
import json

def speak(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()

def check():
    if chec=="y":
         return True
    else:
         return False

        
print("Welcome to weather project by ARYAN. this project has two mode that is Tempertaure and Air Quality")
city = input("Enter the city:")
country = input("Enter the country:")
mode = input("Press 't' for Temperature mode or press 'a' for Air Quality Checker mode\n")
chec = input("Do you want the code to pronouce the weather? If yes press 'y', If not press any other key.\n")

check()

url = f"https://api.weatherapi.com/v1/current.json?key=8dc03494bed148f68d8100045232603&q={city}%20{country}&aqi=yes"
r = requests.get(url)
weather_dic = json.loads(r.text)

if mode == "t":
    degree = input("If you want temperature in Celcius press 'c' and if you want in Fahrenheit press 'f'\n")
    temp_c = weather_dic["current"]["temp_c"]
    temp_f = weather_dic["current"]["temp_f"]
    c = f"Temperature in {city} is {temp_c} degree celcius"
    f = f"Temperature in {city} is {temp_f} degree fahrenheit"

    if degree=="c":
        print(c)
        if check():
            speak(c)
    elif degree=="f":
        print(f)
        if check():
            speak(c)

elif mode=="a":
    co = round(weather_dic["current"]["air_quality"]["co"],2)
    no2 = round(weather_dic["current"]["air_quality"]["no2"],2)
    o3 = round(weather_dic["current"]["air_quality"]["o3"],2)
    so2 = round(weather_dic["current"]["air_quality"]["so2"],2)
    pm2_5 = round(weather_dic["current"]["air_quality"]["pm2_5"],2)
    pm10 = round(weather_dic["current"]["air_quality"]["pm10"],2)

    co_p = f"The value of CO in {city} is {no2}"
    no2_p = f"The value of NO2 in {city} is {no2}"
    o3_p = f"The value of O3 in {city} is {o3}"
    so2_p = f"The value of SO2 in {city} is {so2} "
    pm_p = f"The value of PM2.5 in {city} is {pm2_5}"
    pm10_p = f"The value of PM10 in {city} is {pm10}"
    
    print(co_p)
    print(no2_p)
    print(o3_p)
    print(so2_p)
    print(pm_p)
    print(pm10_p)

    

    if pm10<40:
        print(f"Air quality of {city} is GOOD")
        if check():
            speak(f"Air quality of {city} is good")
        else:
            pass
    elif pm10<=80:
        print(f"Air quality of {city} is FAIR")
        if check():
            speak(f"Air quality of {city} is fair")
        else:
            pass
    elif pm10<=120:
        print(f"Air quality of {city} is POOR")
        if check():
            speak(f"Air quality of {city} is poor")
        else:
            pass
    else:
        print(f"Air quality of {city} is VERY POOR")
        if check():
            speak(f"Air quality of {city} is very poor")
        else:
            pass

    if check():
        speak(co_p)
        speak(no2_p)
        speak(o3_p)
        speak(so2_p)
        speak(pm_p)
        speak(pm10_p)
    else:
        pass

else:
    print("INVALID INPUT")