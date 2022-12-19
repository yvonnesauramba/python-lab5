import requests

# программа которая показывает погоду, влажность и давление в указанном городе
api_key = "d2e762e440c8c3244c368b0948f523cb"
city_name = "Danvers"
units = "metric"  # единицы измерения в градусах Цельсия

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units={units}&appid={api_key}"
response = requests.get(url)

data = response.json()

print(f"Weather in {city_name}: {data['weather'][0]['main']}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Pressure: {data['main']['pressure']} hPa")



# Альтернативное допзадание
api_key = '6hsjmhJkPin2XUYnrqlU107Fh0M6E5QiSTWQxGEp'

# Сделайте запрос на получение к NASA API
response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')

# Проанализируйте ответ в виде JSON
data = response.json()

# Напечатать заголовок и описание фотографии
print(data['title'])
print(data['explanation'])

# Отобразить фотографию
from IPython import display
display.Image(url=data['hdurl'])