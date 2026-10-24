from PyQt6.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGroupBox

class Scherm1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()

        titel = QLabel("Welkom bij de Shuttlebus App")
        layout.addWidget(titel)

        self.nieuwstekst = QLabel("Hier komt het nieuws van de shuttlebus te staan.")
        # layout.addWidget(self.nieuwstekst)

        self.nieuwsinvoer = QLineEdit()
        layout.addWidget(self.nieuwsinvoer)

        nieuwsknop = QPushButton("Nieuws bericht toevoegen")
        nieuwsknop.clicked.connect(self.toon_nieuws)
        layout.addWidget(nieuwsknop)

        self.setLayout(layout)

        leegknop = QPushButton("Leegmaken")
        leegknop.clicked.connect(self.clear_nieuws)

        nieuws_kaart = QGroupBox("Laatste nieuws")
        kaart_layout = QVBoxLayout()
        kaart_layout.addWidget(self.nieuwstekst)
        nieuws_kaart.setLayout(kaart_layout)
        layout.addWidget(nieuws_kaart)
        
        invoerrij = QHBoxLayout()
        invoerrij.addWidget(QLabel("Voer hier uw nieuwsbericht in:"))
        invoerrij.addWidget(self.nieuwsinvoer, 1)
        invoerrij.addWidget(nieuwsknop)
        invoerrij.addWidget(leegknop)
        layout.addLayout(invoerrij)

        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addStretch()

    def toon_nieuws(self):
        bericht = self.nieuwsinvoer.text().strip()
        if bericht != "":
            self.nieuwstekst.setText(bericht)
        else: 
            self.nieuwstekst.setText("Geen nieuwsbericht ingevoerd.")

    def clear_nieuws(self):
        self.nieuwstekst.setText("Hier komt het nieuws van de shuttlebus te staan.")
        self.nieuwsinvoer.clear()
