# Raspberry-Temperatursensor
# Projektbeschreibung
Dieses Projekt ermöglicht die Messung von Temperaturen mithilfe eines Raspberry Pi und eines Temperatursensors. Die gemessenen Daten werden in Echtzeit erfasst und in einer visuellen Darstellung angezeigt. Dies ist besonders nützlich für Umgebungen, in denen eine präzise Überwachung der Temperatur erforderlich ist, wie beispielsweise in Serverräumen, Gewächshäusern oder Heimautomatisierungsprojekten.

# Funktionalitäten
* Auslesen der aktuellen Temperatur
* Auslesen von Temperaturgraph
# Temperaturmessung
Der angeschlossene Temperatursensor liest kontinuierlich die Temperaturwerte aus der Umgebung.
# Echtzeitüberwachung
Die gemessenen Daten werden in Echtzeit erfasst und können sofort visualisiert werden.
# Visuelle Darstellung
Die Temperaturdaten werden in einer übersichtlichen grafischen Benutzeroberfläche dargestellt, um Benutzern eine einfache Interpretation zu ermöglichen.
# Anpassbare Schwellenwerte
Benutzer können Schwellenwerte festlegen, um Alarme zu erhalten, wenn die Temperatur bestimmte Grenzen überschreitet.
# Hardware-Anforderungen
Raspberry Pi (getestet mit Raspberry Pi 3 und neueren Modellen)
Temperatursensor (z.B., DS18B20)
Verbindungskabel
# Software-Anforderungen
Raspbian (oder ein vergleichbares Betriebssystem) auf dem Raspberry Pi installiert
Python 3.x
# Bibliotheken
RPi.GPIO, w1thermsensor
Webbrowser für die Anzeige der visuellen Darstellung
# Installation
# Hardware anschließen
Verbinden Sie den Temperatursensor mit dem Raspberry Pi entsprechend den Spezifikationen des Sensors.
# Software installieren
Führen Sie das Installations-Script aus, um die erforderlichen Bibliotheken und die Anwendung zu installieren.
# Konfiguration
Passen Sie bei Bedarf die Konfigurationsdatei an, um Schwellenwerte und andere Einstellungen festzulegen.
# Starten Sie die Anwendung
Führen Sie das Hauptprogramm aus, um die Temperaturmessung zu starten und die visuelle Darstellung aufzurufen.
Beitrag und Mitwirkung
Beiträge und Vorschläge sind willkommen! Wenn Sie dazu beitragen möchten, erstellen Sie einfach eine Fork dieses Repositories, machen Sie Ihre Änderungen und reichen Sie dann eine Pull-Anfrage ein.

# Ressourcen
* [Node-RED Dokumentation](https://nodered.org/docs/)
* [Raspberry Pi Dokumentation](https://www.raspberrypi.org/documentation/)

# Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Lizenzdatei.

# Autoren
* Steffen Schneider (@Stefn92)
* Adrian Waldthaler (@deradi07)
* Lucas Klein (@LucasVhG)
* Nils Akelbein (@nils0815)

# Schlusswort
Vielen Dank für Ihre Unterstützung und viel Spaß beim Temperaturmessen mit Ihrem Raspberry Pi!
