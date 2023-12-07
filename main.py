from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

temperaturenListe = [5, 19, 2, 5, 3, 8, 12, 3, 24, 5, 6, 5, 8, 4, 12, 13, 16, 9, 11, 10, 4, 7, 12, 0]

fenster = Tk()
fenster.title("Temperaturmesser")
fenster.geometry("500x500")

uhrzeiten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

plt.plot(uhrzeiten, temperaturenListe)
plt.title("Temperaturmesser")
plt.scatter(uhrzeiten, temperaturenListe, color='red')
plt.xlabel("Stunde")
plt.ylabel("Temperaturen (°C)")
plt.show()
