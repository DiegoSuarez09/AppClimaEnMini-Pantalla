import requests
from datetime import datetime, timedelta

# Función para obtener el pronóstico del tiempo
def get_weather_forecast(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Datos de ubicación
lat = -27.48
lon = -58.84

# Clave de API de OpenWeatherMap
api_key = "2823f80e875f52e9a8aba4e1ed7a3a0b"  # Reemplaza 'TU_CLAVE_API' con tu propia clave de API

# Obtener el pronóstico del tiempo
forecast_data = get_weather_forecast(lat, lon, api_key)

# Obtener la fecha actual y la fecha de mañana
today = datetime.now().date()
tomorrow = today + timedelta(days=1)
print(today)

# Procesar los datos y mostrar solo los pronósticos de hoy y mañana
for forecast in forecast_data['list']:
    # Obtener la fecha y hora del pronóstico
    dt_txt = forecast['dt_txt']
    forecast_date = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
    
    # Verificar si el pronóstico es para hoy o mañana
    if forecast_date.date() == today or forecast_date.date() == tomorrow:
        hora_exacta = forecast_date.strftime('%H:%M')  # Convertir a hora exacta
        temperatura = forecast['main']['temp']
        humedad = forecast['main']['humidity']
        descripcion_clima = forecast['weather'][0]['description']
        velocidad_viento = forecast['wind']['speed']
        # Puedes agregar más datos según sea necesario

        print(f"Fecha: {forecast_date.date()}")
        print(f"Hora exacta: {hora_exacta}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Humedad: {humedad}%")
        print(f"Descripción del clima: {descripcion_clima}")
        print(f"Velocidad del viento: {velocidad_viento} m/s")
        print("-----")
