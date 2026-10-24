from PyQt6.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGroupBox

# Scherm1 erft de mogelijkheden van QWidget.
class Scherm1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # De hoofdindeling plaatst onderdelen onder elkaar.
        layout = QVBoxLayout()

        titel = QLabel("Welkom bij de Shuttlebus App")
        layout.addWidget(titel)

        # Met self kunnen andere methodes dit tekstonderdeel bereiken.
        self.nieuwstekst = QLabel("Hier komt het nieuws van de shuttlebus te staan.")

        self.nieuwsinvoer = QLineEdit()
        layout.addWidget(self.nieuwsinvoer)

        # Een klik voert toon_nieuws uit.
        nieuwsknop = QPushButton("Nieuws bericht toevoegen")
        nieuwsknop.clicked.connect(self.toon_nieuws)
        layout.addWidget(nieuwsknop)

        # Koppel de hoofdindeling aan dit scherm.
        self.setLayout(layout)

        leegknop = QPushButton("Leegmaken")
        leegknop.clicked.connect(self.clear_nieuws)

        # De nieuwskaart krijgt een eigen indeling met het nieuwslabel.
        nieuws_kaart = QGroupBox("Laatste nieuws")
        kaart_layout = QVBoxLayout()
        kaart_layout.addWidget(self.nieuwstekst)
        nieuws_kaart.setLayout(kaart_layout)
      

        
        # De Parkinformariekaart 
        parkinfo_kaart = QGroupBox("Parkinformatie")
        parkinfo_layout = QVBoxLayout()
        parkinfo_layout.addWidget(QLabel("Het park opent om 09:00 uur."))
        parkinfo_kaart.setLayout(parkinfo_layout)
       

        # Links en Rechts een kaart
        links_rechts_layout = QHBoxLayout()
        links_rechts_layout.addWidget(nieuws_kaart)
        links_rechts_layout.addWidget(parkinfo_kaart)
        layout.addLayout(links_rechts_layout)


        # Plaats de uitleg, invoer en knoppen naast elkaar.
        invoerrij = QHBoxLayout()
        invoerrij.addWidget(QLabel("Voer hier uw nieuwsbericht in:"))
        invoerrij.addWidget(self.nieuwsinvoer, 1)  # Laat het invoerveld meegroeien.
        invoerrij.addWidget(nieuwsknop)
        invoerrij.addWidget(leegknop)
        layout.addLayout(invoerrij)

        # Afstand tussen onderdelen en ruimte langs de schermranden.
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # De overgebleven verticale ruimte komt onder de onderdelen.
        layout.addStretch()

    def toon_nieuws(self):
        # Lees de invoer en verwijder spaties aan het begin en einde.
        bericht = self.nieuwsinvoer.text().strip()

        # Toon het bericht als er tekst overblijft, anders een melding.
        if bericht != "":
            self.nieuwstekst.setText(bericht)
        else:
            self.nieuwstekst.setText("Geen nieuwsbericht ingevoerd.")

    def clear_nieuws(self):
        # Herstel de begintekst en maak het invoerveld leeg.
        self.nieuwstekst.setText("Hier komt het nieuws van de shuttlebus te staan.")
        self.nieuwsinvoer.clear()