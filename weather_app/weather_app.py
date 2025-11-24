import requests
import os

API_KEY = os.environ.get('OPENWEATHER_API_KEY')  # set this in your environment for safety

def get_weather(city):
    if not API_KEY:
        print('Please set the OPENWEATHER_API_KEY environment variable (see README).')
        return
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if data.get('cod') != 200:
            print('Error:', data.get('message'))
            return
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']
        print(f'City: {city}\nTemperature: {temp} °C\nHumidity: {humidity}%\nCondition: {desc}')
    except Exception as e:
        print('Request failed:', e)

def main():
    city = input('Enter city name (e.g., Bengaluru): ').strip()
    get_weather(city)

if __name__ == '__main__':
    main()
