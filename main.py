import re
import datetime
import psycopg2
import time

#path = "c:/users/sschneider/test.txt"
path = "/sys/bus/w1/devices/28-0000092b9435/w1_slave"
temp = 0
zeit = datetime.datetime.now()
zeitformat = zeit.strftime("%H:%M:%S")

conn = psycopg2.connect(
        dbname="tempsens",
        user="postgres",
        password="AdminAdmin",
        host="127.0.0.1",
        port="5432"
    )

def getTemperatureFromFile():
    # Die aktuelle Zeit wo die Temperatur gemessen wurde
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
                print("Gefundene Temperatur: ", wert)
                temp = wert
                # Hier kannst du weitere Verarbeitungsschritte durchführen, z.B. Wert in eine Variable speichern


def writeToDatabase():
    cur = conn.cursor()

    # SQL-Befehl zum Einfügen eines Werts
    sql = "INSERT INTO data (temperature, time) VALUES (%s)"

    # Wert, den du einfügen möchtest
    wert1 = temp
    wert2 = zeitformat

    # Wert in die Datenbank einfügen
    cur.execute(sql, (wert1, wert2))

    # Änderungen in der Datenbank bestätigen
    conn.commit()

    # Cursor schließen
    cur.close()

    # Verbindung zur Datenbank schließen
    conn.close()

def runProgram():
    while True:
        getTemperatureFromFile()
        writeToDatabase()
        time.sleep(60)

