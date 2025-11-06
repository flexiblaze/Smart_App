import requests
import urllib3


# waarschuwingen
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_current_weather():
    # utrecht weer
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current_weather=true"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        #checking
        if "current_weather" not in data or "temperature" not in data["current_weather"]:
            print("Onverwacht antwoord")
            return

        temp = data["current_weather"]["temperature"]

        if temp < -80 or temp > 80:
            print("Onrealistische temperatuur")
        else:
            print(f"Huidige temperatuur in Utrecht: {temp}°C")

    except requests.exceptions.Timeout:
        print("De API duurde te lang om te antwoorden (timeout)")
    except requests.exceptions.RequestException as e:
        print("Kan weerdata niet ophalen")
        print("Fout:", e)
    except Exception as e:
        print("Onverwachte fout:", e)

def get_inspirational_quote():
    #quote
    url = "https://api.quotable.io/random"
    try:
        # Let op: verify=False voorkomt SSL-fouten
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        data = response.json()

        print("\n✨ Inspirerende Quote van de Dag ✨")
        print(f"\"{data['content']}\" — {data['author']}\n")

    except requests.exceptions.Timeout:
        print("De quote API duurde te lang om te antwoorden (timeout).")
    except requests.exceptions.RequestException as e:
        print("Kon geen quote ophalen.")
        print("Fout:", e)