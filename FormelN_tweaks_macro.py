import time
import keyboard  # Installieren mit: pip install keyboard

def main():
    print("--- FormelN tweak macro ---")
    
    # 1. Taste abfragen, die getippt werden soll
    taste_zum_druecken = input("Welche Taste soll das Makro tippen? (z.B. a, b, enter, space): ").strip()
    
    # 2. Anzahl abfragen und auf maximal 150 begrenzen
    try:
        wiederholungen = int(input("Wie oft soll die Taste gedrückt werden? (Maximal 150): "))
        if wiederholungen > 150:
            print("Das Maximum ist 150. Die Anzahl wurde auf 150 gesetzt.")
            wiederholungen = 150
        elif wiederholungen < 1:
            print("Ungültige Anzahl. Setze auf 1.")
            wiederholungen = 1
    except ValueError:
        print("Keine gültige Zahl eingegeben. Setze auf 10 Wiederholungen.")
        wiederholungen = 10

    # 3. Auslöser-Taste abfragen
    start_taste = input("Welche Taste soll das Makro STARTEN? (z.B. f4, f8, x): ").strip()

    print(f"\n[Bereit] Drücke die Taste '{start_taste}', um das Makro zu starten...")
    print("Zum Beenden des gesamten Programms drücke 'enter'.")

    while True:
        # Warten, bis die Start-Taste gedrückt wird
        if keyboard.is_pressed(start_taste):
            print(f"\n[Start] Tippe '{taste_zum_druecken}' genau {wiederholungen} Mal...")
            
            # Kurz warten, damit die Start-Taste nicht mitgetippt wird
            time.sleep(0.3) 
            
            # Das eigentliche Makro (Schleife)
            for i in range(wiederholungen):
                keyboard.press_and_release(taste_zum_druecken)
                time.sleep(0.05)  # Kleine Pause (50ms) zwischen den Klicks, damit Windows hinterherkommt
                
            print("[Fertig] Makro ausgeführt. Bereit für den nächsten Start.")
            time.sleep(0.5)  # Schutz vor Mehrfachauslösern

        # Programm komplett beenden mit ENTER
        if keyboard.is_pressed('enter'):
            print("Programm beendet.")
            break

        time.sleep(0.01) # CPU-Entlastung

if __name__ == "__main__":
    main()
