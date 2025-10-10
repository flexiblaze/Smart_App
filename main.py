from apps.weerstation import weerstation
from apps.smart_app_controller import smart_app_controller
from utils import get_current_weather, get_nasa_apod
from colorama import init, Fore, Style

init(autoreset=True)

NASA_API_KEY = "dMS77MK4sQXhi7z4Xb6XBJJhIpy5Nu6ZPUofggpR"  # api key


# ASCII
logo = f"""
{Fore.CYAN}{Style.BRIGHT}$$\\      $$\\ $$$$$$$$\\  $$$$$$\\ $$$$$$$$\\ $$\\   $$\\ $$$$$$$$\\ $$$$$$$\\         
$$ | $\\  $$ |$$  _____|$$  __$$\\__$$  __|$$ |  $$ |$$  _____|$$  __$$\\       
$$ |$$$\\ $$ |$$ |      $$ /  $$ |  $$ |   $$ |  $$ |$$ |      $$ |  $$ |      
$$ $$ $$\\$$ |$$$$$\\    $$$$$$$$ |  $$ |   $$$$$$$$ |$$$$$\\    $$$$$$$  |      
$$$$  _$$$$ |$$  __|   $$  __$$ |  $$ |   $$  __$$ |$$  __|   $$  __$$<       
$$$  / \\$$$ |$$ |      $$ |  $$ |  $$ |   $$ |  $$ |$$ |      $$ |  $$ |      
$$  /   \\$$ |$$$$$$$$\\ $$ |  $$ |  $$ |   $$ |  $$ |$$$$$$$$\\ $$ |  $$ |      
\\__/     \\__|\\________|\\__|  \\__|  \\__|   \\__|  \\__|\\________|\\__|  \\__|      
"""

def main():
    print(logo)
    print(Fore.YELLOW + Style.BRIGHT + "Welkom bij de Smart App!\n")

    while True:
        print(Fore.CYAN + Style.BRIGHT + "--- Smart App Hoofdmenu ---")
        print(Fore.GREEN + "1. Weerstation")
        print(Fore.GREEN + "2. Smart App Controller")
        print(Fore.GREEN + "3. Huidige temperatuur Utrecht")
        print(Fore.GREEN + "4. Stoppen")
        print(Fore.GREEN + "5. NASA APOD (ruimtefoto van de dag)")

        keuze = input(Fore.YELLOW + "Maak een keuze (1-5): ")

        if keuze == "1":
            weerstation()
        elif keuze == "2":
            smart_app_controller()
        elif keuze == "3":
            get_current_weather()
        elif keuze == "4":
            print(Fore.MAGENTA + "Programma afgesloten. Tot ziens!")
            break
        elif keuze == "5":
            get_nasa_apod(NASA_API_KEY)
        else:
            print(Fore.RED + "Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()
