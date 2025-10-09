import requests

# Open-Meteo API: huidige temperatuur Utrecht
def get_temp_utrecht():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=52.09&longitude=5.12&current_weather=true"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["current_weather"]["temperature"]
    except Exception as e:
        print(f"Fout bij ophalen weerdata: {e}")
        return None

# Willekeurige inspirerende quote
def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        response.raise_for_status()
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    except Exception as e:
        print(f"Kon geen quote ophalen: {e}")
        return None

# NASA APOD (Astronomy Picture of the Day)
def get_nasa_apod(api_key):
    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return f"Titel: {data['title']}\nURL: {data['url']}\nUitleg: {data['explanation']}"
    except Exception as e:
        print(f"Kon NASA APOD niet ophalen: {e}")
        return None
