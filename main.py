from tkinter import *
import matplotlib.pyplot as plt

aktuelleTemperatur = 0
temperaturenListe = [5, 19, 2, 5, 3, 8]

fenster = Tk()
fenster.title("Temperaturmesser")
fenster.geometry("500x500")

# Label zur Darstellung der aktuellen Temperatur
tempStr = str(aktuelleTemperatur)
temperaturLabel = Label(fenster, text="Aktuelle Temperatur: " + tempStr + "°C", anchor=N, relief=RAISED, font=('Helvetica', 15))

# Daten für den Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot erstellen
plt.plot(x, y)
# Achsenbeschriftungen hinzufügen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

# Titel hinzufügen
plt.title('Einfacher Linienplot')

# Plot anzeigen
plt.show()
fenster.mainloop()

def setAktuelleTemperatur(temp):
    aktuelleTemperatur = temp

def setAlleTemperaturen(temps):
    temp_Liste = temps
    










