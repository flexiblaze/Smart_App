def aantal_dagen(inputFile):
    try:
        with open(inputFile, "r") as f:
            regels = f.readlines()

        if len(regels) <= 1:
            print("Geen data gevonden in het invoerbestand.")
            return 0

        data_regels = [r.strip() for r in regels[1:] if r.strip()]

        datums = [r.split()[0] for r in data_regels]

        print(f"\nEr zijn {len(datums)} dagen in het bestand.")
        print("Beschikbare datums:")
        print(", ".join(datums))
        print()

        return len(datums)

    except FileNotFoundError:
        print("Bestand niet gevonden. Controleer de bestandsnaam of locatie.")
        return 0
    except Exception as e:
        print("Onverwachte fout:", e)
        return 0


def auto_bereken(inputFile, outputFile):
    #Leest het invoerbestand
    try:
        with open(inputFile, "r") as f:
            regels = [r.strip() for r in f.readlines()][1:]  # sla header over

        if not regels:
            print("Geen datarijen gevonden in het invoerbestand.")
            return

        uitvoerregels = []

        for regel in regels:
            try:
                datum, personen, setpoint, buiten, neerslag = regel.split()
                personen = int(personen)
                setpoint = float(setpoint)
                buiten = float(buiten)
                neerslag = float(neerslag)
            except ValueError:
                print(f"Ongeldige gegevens in regel: '{regel}', overgeslagen.")
                continue

            # Controle op realistische waarden
            if not (-30 <= buiten <= 50 and 5 <= setpoint <= 30 and 0 <= neerslag <= 500):
                print(f"Onrealistische waarden op datum {datum}, overgeslagen.")
                continue

            # CV-ketel logica
            verschil = setpoint - buiten
            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            # ventilatie logica
            ventilatie = min(personen + 1, 4)

            # bewatering logica
            bewatering = neerslag < 3

            uitvoerregels.append(f"{datum};{cv};{ventilatie};{bewatering}")

        # bestand wegschrijven
        with open(outputFile, "w") as f:
            for regel in uitvoerregels:
                f.write(regel + "\n")

        print(f"Automatisch berekend en opgeslagen in '{outputFile}'.")

    except FileNotFoundError:
        print("Invoerbestand niet gevonden.")
    except Exception as e:
        print("Onverwachte fout tijdens berekenen:", e)


def overwrite_settings(outputFile):
    #overschirijven
    try:
        with open(outputFile, "r") as f:
            regels = [r.strip() for r in f.readlines()]
        if not regels:
            print("Uitvoerbestand is leeg.")
            return -1
    except FileNotFoundError:
        print("Uitvoerbestand niet gevonden.")
        return -1

    datum = input("Welke datum wil je aanpassen (dd-mm-jjjj)? ").strip()
    gevonden = False

    for i, regel in enumerate(regels):
        if regel.startswith(datum):
            gevonden = True
            parts = regel.split(";")
            print(f"Huidige waarden: CV={parts[1]}, Ventilatie={parts[2]}, Bewatering={parts[3]}")

            systeem = input("Welk systeem wil je aanpassen? (1=CV, 2=Ventilatie, 3=Bewatering): ").strip()
            if systeem not in ["1", "2", "3"]:
                print("Ongeldig systeem gekozen.")
                return -3

            nieuwe_waarde = input("Nieuwe waarde: ").strip()

            try:
                if systeem == "1":  # CV-ketel
                    waarde = int(nieuwe_waarde)
                    if 0 <= waarde <= 100:
                        parts[1] = str(waarde)
                    else:
                        print("Ongeldige waarde voor CV (0–100).")
                        return -3

                elif systeem == "2":  # Ventilatie
                    waarde = int(nieuwe_waarde)
                    if 0 <= waarde <= 4:
                        parts[2] = str(waarde)
                    else:
                        print("Ongeldige waarde voor ventilatie (0–4).")
                        return -3

                elif systeem == "3":  # Bewatering
                    if nieuwe_waarde == "1":
                        parts[3] = "True"
                    elif nieuwe_waarde == "0":
                        parts[3] = "False"
                    else:
                        print("Ongeldige waarde voor bewatering (0 of 1).")
                        return -3

            except ValueError:
                print("Ongeldige invoer, gebruik cijfers.")
                return -3

            regels[i] = ";".join(parts)
            break

    if not gevonden:
        print("Datum niet gevonden in uitvoerbestand.")
        return -1

    with open(outputFile, "w") as f:
        for regel in regels:
            f.write(regel + "\n")

    print("Waarde succesvol aangepast.")
    return 0


def smart_app_controller():
    #Smart App Controller
    print("Welkom bij de Smart App Controller!\n")

    while True:
        print("--- Smart App Controller Menu ---")
        print("1. Toon aantal dagen in invoerbestand")
        print("2. Autobereken actuatoren en schrijf naar uitvoerbestand")
        print("3. Overschrijf een waarde in uitvoerbestand")
        print("4. Terug naar hoofdmenu")

        keuze = input("Maak een keuze (1–4): ").strip()

        if keuze == "1":
            aantal_dagen("input_data.txt")
        elif keuze == "2":
            auto_bereken("input_data.txt", "output_data.txt")
        elif keuze == "3":
            overwrite_settings("output_data.txt")
        elif keuze == "4":
            print("Terug naar hoofdmenu...")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")
