from apps.weerstation import weerstation
from apps.smart_app_controller import smart_app_controller
from utils import get_temp_utrecht, get_random_quote, get_nasa_apod

NASA_API_KEY = "dMS77MK4sQXhi7z4Xb6XBJJhIpy5Nu6ZPUofggpR"  # vervang door je eigen key

def main_menu():
    while True:
        print("\n--- Smart App Hoofdmenu ---")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Huidige temperatuur Utrecht")
        print("4. Stoppen")
        print("5. Inspirerende quote")
        print("6. NASA APOD (ruimtefoto van de dag)")

        keuze = input("Maak een keuze (1-6): ")

        try:
            keuze = int(keuze)
        except ValueError:
            print("Ongeldige invoer, voer een getal in 1-6")
            continue

        if keuze == 1:
            weerstation()
        elif keuze == 2:
            smart_app_controller()
        elif keuze == 3:
            temp = get_temp_utrecht()
            if temp is not None:
                print(f"Huidige temperatuur in Utrecht: {temp}°C")
            else:
                print("Kon temperatuur niet ophalen.")
        elif keuze == 4:
            print("Applicatie gestopt.")
            break
        elif keuze == 5:
            quote = get_random_quote()
            if quote:
                print(quote)
            else:
                print("Kon geen quote ophalen.")
        elif keuze == 6:
            apod = get_nasa_apod(NASA_API_KEY)
            if apod:
                print(apod)
            else:
                print("Kon NASA APOD niet ophalen.")
        else:
            print("Kies een getal tussen 1 en 6")

if __name__ == "__main__":
    main_menu()
