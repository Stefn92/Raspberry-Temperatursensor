import re
import datetime
import psycopg2
import time

#path = "c:/users/sschneider/test.txt"
path = "/sys/bus/w1/devices/28-0000092b9435/w1_slave"
temp = 0
zeit = datetime.datetime.now()
zeitformat = zeit.strftime("%H:%M:%S")


def getTemperatureFromFile():
    # Die aktuelle Zeit wo die Temperatur gemessen wurde
    global zeit
    global zeitformat
    zeit = datetime.datetime.now()
    zeitformat = zeit.strftime("%H:%M:%S")
    with open(path, 'r') as file:
        # Durch die Datei Zeile für Zeile iterieren
        for line in file:
            # Durchsuche die Zeile nach dem Muster 't=' gefolgt von Zahlen
            match = re.search(r't=(\d+)', line)
            # Falls ein Match gefunden wurde
            if match:
                # Extrahiere den gefundenen Wert und entferne das 't='
                wert = match.group(1)
                formatierter_wert = wert[:2] + '.' + wert[2:]
                wert = formatierter_wert
                print(wert)
                print("Temperatur aus Datei extrahiert")
                global temp
                temp = wert
                # Hier kannst du weitere Verarbeitungsschritte durchführen, z.B. Wert in eine Variable speichern


def writeToDatabase():
    conn = psycopg2.connect(
        dbname="tempsens",
        user="postgres",
        password="AdminAdmin",
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()

    # SQL-Befehl zum Einfügen eines Werts
    sql = "INSERT INTO data (temperature, time) VALUES (%s, %s)"

    # Wert, den du einfügen möchtest
    wert1 = str(temp)
    wert2 = str(zeitformat)

    # Wert in die Datenbank einfügen
    cur.execute(sql, (wert1, wert2))

    # Änderungen in der Datenbank bestätigen
    conn.commit()
    print("Daten in Datenbank eingefügt")

    # Cursor schließen
    cur.close()

    # Verbindung zur Datenbank schließen
    conn.close()

def runProgram():
    while True:
        getTemperatureFromFile()
        writeToDatabase()
        time.sleep(5)


runProgram()