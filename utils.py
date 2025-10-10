import requests

def get_current_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['current_weather']['temperature']
        print(f"Huidige temperatuur in Utrecht: {temp}°C")
    else:
        print("Kan weerdata niet ophalen.")

#nasa
def get_nasa_apod(api_key="DEMO_KEY"):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Datum: {data['date']}")
        print(f"Titel: {data['title']}")
        print(f"Uitleg: {data['explanation']}\n")
        print(f"Bekijk de afbeelding hier: {data['url']}")
    except requests.exceptions.RequestException as e: #fouten
        print("Kan NASA APOD niet ophalen.")
        print("Fout:", e)

