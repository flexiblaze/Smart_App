# Sprint 2: Smart App Controller

# Functie 1: aantal dagen in inputbestand tellen
def aantal_dagen(inputFile):
    try:
        with open(inputFile, 'r') as file:
            regels = file.readlines()
        datarijen = [line for line in regels[1:] if line.strip() != ""]
        aantal = len(datarijen)
        print(f"Er zijn {aantal} dagen in het bestand.")
        return aantal
    except FileNotFoundError:
        print("Fout: het opgegeven bestand bestaat niet.")
        return 0


# Functie 2: actuatoren automatisch berekenen en naar outputbestand schrijven
def auto_bereken(inputFile, outputFile):
    try:
        with open(inputFile, 'r') as infile:
            regels = infile.readlines()
        datarijen = [line for line in regels[1:] if line.strip() != ""]

        with open(outputFile, 'w') as outfile:
            for line in datarijen:
                datum, numPeople, tempSetpoint, tempOutside, precip = line.split()
                numPeople = int(numPeople)
                tempSetpoint = float(tempSetpoint)
                tempOutside = float(tempOutside)
                precip = float(precip)

                # CV-ketel
                verschil = tempSetpoint - tempOutside
                if verschil >= 20:
                    cv = 100
                elif verschil >= 10:
                    cv = 50
                else:
                    cv = 0

                # Ventilatie
                vent = min(numPeople + 1, 4)

                # Bewatering
                bewatering = True if precip < 3 else False

                # Schrijf naar outputbestand
                outfile.write(f"{datum};{cv};{vent};{bewatering}\n")

        print(f"Outputbestand '{outputFile}' succesvol aangemaakt.")

    except FileNotFoundError:
        print("Fout: inputbestand bestaat niet.")


# Functie 3: actuatorwaarden overschrijven
def overwrite_settings(outputFile):
    try:
        with open(outputFile, 'r') as f:
            regels = [line.strip() for line in f.readlines()]

        datum = input("Welke datum wil je aanpassen (dd-mm-jjjj)? ")
        gevonden = False

        for i, line in enumerate(regels):
            if line.startswith(datum):
                gevonden = True
                parts = line.split(';')
                print(f"Huidige waarden: CV={parts[1]}, Ventilatie={parts[2]}, Bewatering={parts[3]}")
                systeem = input("Welk systeem wil je aanpassen? (1=CV, 2=Ventilatie, 3=Bewatering) ")
                nieuwe_waarde = input("Nieuwe waarde: ")

                if systeem == '1':  # CV-ketel
                    waarde = int(nieuwe_waarde)
                    if 0 <= waarde <= 100:
                        parts[1] = str(waarde)
                    else:
                        print("Ongeldige waarde")
                        return -3
                elif systeem == '2':  # Ventilatie
                    waarde = int(nieuwe_waarde)
                    if 0 <= waarde <= 4:
                        parts[2] = str(waarde)
                    else:
                        print("Ongeldige waarde")
                        return -3
                elif systeem == '3':  # Bewatering
                    if nieuwe_waarde == '1':
                        parts[3] = 'True'
                    elif nieuwe_waarde == '0':
                        parts[3] = 'False'
                    else:
                        print("Ongeldige waarde")
                        return -3
                else:
                    print("Ongeldig systeem gekozen")
                    return -3

                regels[i] = ';'.join(parts)
                break

        if not gevonden:
            print("Datum niet gevonden")
            return -1

        with open(outputFile, 'w') as f:
            for line in regels:
                f.write(line + '\n')

        print("Waarde succesvol aangepast.")
        return 0

    except FileNotFoundError:
        print("Outputbestand bestaat niet.")
        return -1


# Functie 4: Menu
def smart_app_controller():
    inputFile = "input_data.txt"
    outputFile = "output_data.txt"

    while True:
        print("\n--- Smart App Controller Menu ---")
        print("1. Hoeveel dagen zijn er aanwezig?")
        print("2. Autobereken alle actuatoren en schrijf naar file")
        print("3. Waarde overschrijven in outputbestand")
        print("4. Stoppen")

        keuze = input("Maak een keuze (1-4): ")

        if keuze == '1':
            aantal_dagen(inputFile)
        elif keuze == '2':
            auto_bereken(inputFile, outputFile)
        elif keuze == '3':
            overwrite_settings(outputFile)
        elif keuze == '4':
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze. Kies 1-4.")


if __name__ == "__main__":
    with open("../input_data.txt", "r") as f:
        regels = f.readlines()
        print(regels)

    # Daarna start je pas het menu
    smart_app_controller()

