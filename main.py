import requests
from PIL import Image, ImageDraw, ImageFont
import shutil

# Función para obtener datos del clima desde la API de OpenWeatherMap
def get_weather_data(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Función para generar una imagen con la información del clima
def generate_weather_image(weather_data):
    # Crear una nueva imagen en blanco
    img = Image.new('RGB', (400, 200), color=(21, 121, 233 ))
    draw = ImageDraw.Draw(img)
    
    # Fuente para el texto
    font = ImageFont.load_default()
    
    # Escribir la información del clima en la imagen
    draw.text((10, 10), f"Temperatura: {weather_data['main']['temp']}°C", fill=(0, 0, 0), font=font)
    draw.text((10, 30), f"Velocidad del viento: {weather_data['wind']['speed']} m/s", fill=(0, 0, 0), font=font)
    draw.text((10, 50), f"Humedad: {weather_data['main']['humidity']}%", fill=(0, 0, 0), font=font)
    draw.text((10, 70), f"Descripcion: {weather_data['weather'][0]['description']}", fill=(0, 0, 0), font=font)
    
    # Guardar la imagen
    img.save('weather_image2.png')

# Datos de ubicación
lat = -27.48
lon = -58.84

# Clave de API de OpenWeatherMap
api_key = "2823f80e875f52e9a8aba4e1ed7a3a0b"  # Reemplaza 'TU_CLAVE_API' con tu propia clave de API

# Obtener datos del clima
weather_data = get_weather_data(lat, lon, api_key)

# Generar imagen del clima
generate_weather_image(weather_data)

# Ruta de la carpeta del dispositivo donde se mostrarán las imágenes
device_folder = r"C:\Users\Public\Pictures\Wacom STU Display\STU530"

# Copiar la imagen a la carpeta del dispositivo
shutil.copy('weather_image2.png', device_folder)
