import speech_recognition as sr
import subprocess

# Funktion zum Ausführen des PowerShell-Befehls
def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True, encoding='utf-8')
        if result.stdout:
            print("Ausgabe:")
            print(result.stdout.strip())
        if result.stderr:
            print("Fehlermeldung:")
            print(result.stderr.strip())
        if not result.stdout and not result.stderr:
            print("Keine Ausgabe.")
    except subprocess.CalledProcessError as e:
        print("Fehler beim Ausführen des Befehls:")
        print(e.stderr)


# Hauptprogramm
def main():
    # Initialisierung des Spracherkenners
    r = sr.Recognizer()

    # Aufnehmen des Spracheingabe des Benutzers
    with sr.Microphone() as source:
        print("Sage einen PowerShell-Befehl...")
        audio = r.listen(source)

    try:
        # Spracherkennung
        command = r.recognize_google(audio)
        print("Erkannter Befehl: " + command)

        # Ausführen des PowerShell-Befehls
        command = "Start-Process -FilePath 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'"
        run_powershell_command(command)

    except sr.UnknownValueError:
        print("Konnte den Befehl nicht verstehen.")
    except sr.RequestError as e:
        print("Fehler bei der Spracherkennung:", str(e))

if __name__ == "__main__":
    main()
