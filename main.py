import re
import datetime
import psycopg2
import time

path = "/sys/bus/w1/devices/28-0000092b9435/w1_slave"
current_temp = 0
current_time = datetime.datetime.now()
current_date = datetime.datetime.today()
time_format = current_time.strftime("%H:%M:%S")
date_format = current_date.strftime("%Y-%m-%d")

def get_temperature_from_file():
    # Die aktuelle Zeit, wo die Temperatur gemessen wurde
    global current_time
    global time_format
    global current_date
    global date_format
    current_time = datetime.datetime.now()
    time_format = current_time.strftime("%H:%M:%S")
    current_date = datetime.datetime.today()
    date_format = current_date.strftime("%Y-%m-%d")
    with open(path, 'r') as file:
        # Durch die Datei Zeile für Zeile iterieren
        for line in file:
            # Durchsuche die Zeile nach dem Muster 't=' gefolgt von Zahlen
            match = re.search(r't=(\d+)', line)
            # Falls ein Match gefunden wurde
            if match:
                # Extrahiere den gefundenen Wert und entferne das 't='
                temp = match.group(1)
                rounded_temp = float(temp[:2] + '.' + temp[2:])
                # Runde den Wert auf eine Nachkommastelle
                rounded_value = round(rounded_temp, 1)
                strTemp = str(rounded_value)
                global current_temp
                current_temp = strTemp

def write_to_database():
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

    temp = str(current_temp)
    time = str(time_format)
    date = str(date_format)

    # Wert in die Datenbank einfügen
    cur.execute(sql, (temp, time, date))

    # Änderungen in der Datenbank bestätigen
    conn.commit()

    # Cursor schließen
    cur.close()

    # Verbindung zur Datenbank schließen
    conn.close()

# Programm wird alle 60 Sekunden ausgeführt
def run_program():
    while True:
        get_temperature_from_file()
        write_to_database()
        time.sleep(60)

run_program()