# Vaak gebruikte handelingen in PyQt6

layout.addWidget(onderdeel)          # Onderdeel toevoegen
layout.addLayout(andere_layout)      # Indelingen combineren
widget.setLayout(layout)             # Widget zijn indeling geven

knop.clicked.connect(self.methode)   # Klik koppelen
self.invoer.text()                   # Invoer lezen
self.label.setText("Nieuwe tekst")   # Tekst veranderen
self.invoer.clear()                  # Invoer leegmaken

| Handeling | Betekenis |
| `label.setText("Nieuws")` | Tekst veranderen |
| `label.text()` | De huidige tekst opvragen |
| `label.clear()` | Tekst leegmaken |
| `label.setWordWrap(True)` | Lange tekst over meerdere regels verdelen |

| Handeling | Betekenis |
| `invoer.text()` | Ingevoerde tekst lezen |
| `invoer.setText("Sara")` | Invoer vanuit je code invullen |
| `invoer.clear()` | Invoer leegmaken |
| `invoer.setPlaceholderText("Naam reisplan")` | Voorbeeldtekst tonen zolang het veld leeg is |
| `invoer.setMaxLength(100)` | Maximumaantal tekens instellen |
| `invoer.setReadOnly(True)` | Invoer zichtbaar houden, maar wijzigen blokkeren |
| `invoer.setFocus()` | De cursor naar dit veld verplaatsen |

| Handeling | Betekenis |
| `knop.setText("Zoeken")` | Knoptekst veranderen |
| `knop.clicked.connect(self.zoeken)` | Een klik koppelen aan een methode |
| `invoer.returnPressed.connect(self.zoeken)` | Enter in het invoerveld koppelen |
| `invoer.textChanged.connect(self.invoer_gewijzigd)` | Reageren wanneer de invoer verandert |

| Handeling | Betekenis |
| `onderdeel.hide()` | Verbergen |
| `onderdeel.show()` | Tonen |
| `onderdeel.setVisible(voorwaarde)` | Tonen als de voorwaarde `True` is |
| `onderdeel.setEnabled(False)` | Bediening uitschakelen |
| `onderdeel.setEnabled(True)` | Bediening inschakelen |
| `onderdeel.setObjectName("nieuwstitel")` | Een naam geven die je bijvoorbeeld in QSS gebruikt |