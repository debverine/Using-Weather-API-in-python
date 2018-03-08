import requests


def weather(city):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    #city = input('City Name :')
    url = api_address + city
    json_data = requests.get(url).json()
    #print(json_data)
    
    weather_description = json_data['weather'][0]['description']
    print("City : "+city)
    print(weather_description)
    temp=json_data['main']['temp']-273.15
    humidity=json_data['main']['humidity']
    print(str(temp)+" C")
    print(str(humidity)+" %")
    

list=["Kolkata","Mumbai","Delhi","Bangalore","Dubai","Ahmedabad"]
for i in list:
    weather(i)
    print("************************")
