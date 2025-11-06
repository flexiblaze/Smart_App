from colorama import Fore, Style, init
init(autoreset=True)

from apps.weerstation import weerstation
from apps.smart_app_controller import smart_app_controller
from utils import get_current_weather, get_inspirational_quote

init(autoreset=True)


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
    print(Fore.YELLOW + Style.BRIGHT + "Welkom bij de WEATHER METER!\n")

    while True:
        print(Fore.CYAN + Style.BRIGHT + "--- WEATHER METER Hoofdmenu ---")
        print(Fore.GREEN + "1. Weerstation")
        print(Fore.GREEN + "2. Home Controller")
        print(Fore.GREEN + "3. Huidige temperatuur Utrecht")
        print(Fore.GREEN + "4. Stoppen")
        print(Fore.GREEN + "5. Inspirerende Quote van de Dag")

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
            get_inspirational_quote()
        else:
            print(Fore.RED + "Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramma handmatig gestopt. Tot ziens!")
