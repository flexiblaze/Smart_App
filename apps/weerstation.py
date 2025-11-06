def Fahrenheit(temp_celsius):
    return 32 + 1.8 * temp_celsius


def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    return temp_celsius - (luchtvochtigheid / 100) * windsnelheid


def weerrapport(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def vraag_temperatuur(dag):
    while True:
        temp_input = input(f"Wat is op dag {dag} de temperatuur[C]: ").strip()
        if temp_input == "":
            print("Invoer mag niet leeg zijn. Probeer opnieuw.")
            continue
        try:
            temp = float(temp_input)
            if -50 <= temp <= 60:
                return temp
            else:
                print("Ongeldige temperatuur, voer iets tussen -50 en 60°C in.")
        except ValueError:
            print("Ongeldige invoer. Gebruik alleen cijfers.")


def vraag_windsnelheid(dag):
    while True:
        wind_input = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ").strip()
        if wind_input == "":
            print("Invoer mag niet leeg zijn. Probeer opnieuw.")
            continue
        try:
            wind = float(wind_input)
            if 0 <= wind <= 60:
                return wind
            else:
                print("Ongeldige windsnelheid, voer iets tussen 0 en 60 m/s in.")
        except ValueError:
            print("Ongeldige invoer. Gebruik alleen cijfers.")


def vraag_vochtigheid(dag):
    while True:
        vocht_input = input(f"Wat is op dag {dag} de vochtigheid[%]: ").strip()
        if vocht_input == "":
            print("Invoer mag niet leeg zijn. Probeer opnieuw.")
            continue
        try:
            vocht = int(vocht_input)
            if 0 <= vocht <= 100:
                return vocht
            else:
                print("Ongeldige vochtigheid, voer iets tussen 0 en 100% in.")
        except ValueError:
            print("Ongeldige invoer Gebruik alleen gehele cijfers.")


def weerstation():
    print("Weerstation Voer weerdata in")
    temperaturen = []

    for dag in range(1, 8):
        temp = vraag_temperatuur(dag)
        wind = vraag_windsnelheid(dag)
        vocht = vraag_vochtigheid(dag)

        temp_f = Fahrenheit(temp)
        gevoel = gevoelstemperatuur(temp, wind, vocht)
        rapport = weerrapport(temp, wind, vocht)

        temperaturen.append(temp)
        gemiddelde = sum(temperaturen) / len(temperaturen)

        # Uitvoer
        print("\n--------------------------------------")
        print(f"Dag {dag}: {temp:.1f}°C ({temp_f:.1f}°F)")
        print(f"Gevoelstemperatuur: {gevoel:.1f}°C")
        print(rapport)
        print(f"Gemiddelde temperatuur tot nu toe: {gemiddelde:.1f}°C")
        print("--------------------------------------")

    print("=== Einde invoer weerstation ===")
