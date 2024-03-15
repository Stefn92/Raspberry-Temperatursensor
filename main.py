import re
import datetime
import psycopg2
import time

path = "/sys/bus/w1/devices/28-0000092b9435/w1_slave"
currentTemp = 0
currentTime = datetime.datetime.now()
currentDate = datetime.datetime.today()
timeFormat = currentTime.strftime("%H:%M:%S")
dateFormat = currentDate.strftime("%Y-%m-%d")

def getTemperatureFromFile():
    # Die aktuelle Zeit, wo die Temperatur gemessen wurde
    global currentTime
    global timeFormat
    global currentDate
    global dateFormat
    currentTime = datetime.datetime.now()
    timeFormat = currentTime.strftime("%H:%M:%S")
    currentDate = datetime.datetime.today()
    dateFormat = currentDate.strftime("%Y-%m-%d")
    with open(path, 'r') as file:
        # Durch die Datei Zeile für Zeile iterieren
        for line in file:
            # Durchsuche die Zeile nach dem Muster 't=' gefolgt von Zahlen
            match = re.search(r't=(\d+)', line)
            # Falls ein Match gefunden wurde
            if match:
                # Extrahiere den gefundenen Wert und entferne das 't='
                value = match.group(1)
                formattedValue = value[:2] + '.' + value[2:]
                value = formattedValue
                print("Temperatur aus Datei extrahiert...")
                global currentTemp
                currentTemp = value

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
    sql = "INSERT INTO data (temperature, time, date) VALUES (%s, %s, %s)"

    temp = str(currentTemp)
    time = str(timeFormat)
    date = str(dateFormat)

    # Wert in die Datenbank einfügen
    cur.execute(sql, (temp, time, date))

    # Änderungen in der Datenbank bestätigen
    conn.commit()
    print("Daten in Datenbank eingefügt...")

    # Cursor schließen
    cur.close()

    # Verbindung zur Datenbank schließen
    conn.close()

# Programm wird alle 5 Sekunden ausgeführt
def runProgram():
    while True:
        getTemperatureFromFile()
        writeToDatabase()
        time.sleep(5)

runProgram()