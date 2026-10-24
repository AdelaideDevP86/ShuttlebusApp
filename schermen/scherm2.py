from PyQt6.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QLabel, QPushButton

class Scherm2(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Dit is scherm 2"))

       
        btn_naar_scherm1 = QPushButton("Naar scherm 1")
        btn_naar_scherm1.clicked.connect(self.open_scherm)
        layout.addWidget(btn_naar_scherm1)

        titel = QLabel("Welkom bij de Shuttlebus App")
        layout.addWidget(titel)

        self.nieuwstekst = QLabel("Hier komt het nieuws van de shuttlebus te staan.")
        layout.addWidget(self.nieuwstekst)

        self.nieuwsinvoer = QLineEdit()
        layout.addWidget(self.nieuwsinvoer)
        self.nieuwsinvoer.setPlaceholderText("Voer hier het nieuwsbericht in")
        btn_nieuws_toevoegen = QPushButton("Nieuws bericht toevoegen")
        layout.addWidget(btn_nieuws_toevoegen)
        btn_nieuws_toevoegen.clicked.connect(self.toon_nieuws)

       

        self.setLayout(layout)

    def open_scherm(self):
        self.main_window.toon_pagina(self.main_window.scherm1)

    def toon_nieuws(self):
        nieuwsbericht = self.nieuwsinvoer.text()
        self.nieuwstekst.setText(nieuwsbericht)
        self.nieuwsinvoer.clear()