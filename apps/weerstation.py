def Fahrenheit(temp_celsius):
    fahrenheit = 32 + 1.8 * temp_celsius
    return fahrenheit

def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoelstemperatuur = temp_celsius - (luchtvochtigheid / 100) * windsnelheid
    return gevoelstemperatuur


def weerrapport(temp_celsius, windsnelheid, luchtvochtigheid):

    gevoel = gevoelstemperatuur(temp_celsius,windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10 :
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10 :
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel >=10 and gevoel < 22:
         return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm Airco aan!"

def weerstation():
    temperaturen = []
    for dag in range(1, 8):
        temp = input(f"Wat is op dag {dag} de temperatuur[C]: ")
        if temp == "":
            print("Bye")
            break
        temp = float(temp)

        wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")
        if wind == "":
            print("Bye")
            break
        wind = float(wind)

        vocht = input(f"Wat is op dag {dag} de vochtigheid[%]: ")
        if vocht == "":
            print("Bye")
            break
        vocht = int(vocht)

        temp_f = Fahrenheit(temp)
        gevoel = gevoelstemperatuur(temp, wind, vocht)
        rapport = weerrapport(temp, wind, vocht)

        temperaturen.append(temp)
        gemiddelde = sum(temperaturen) / len(temperaturen)

        print(f"Het is {temp:.1f}C ({temp_f:.1f}F)")
        print(rapport)
        print(f"Gem. temp tot nu toe is {gemiddelde:.1f}")
        print("=" * 38)