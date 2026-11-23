"""EnerTec – Aufbau des Wasserstoff-Versuchskoffers (Deutsch / English)."""
from pathlib import Path

import streamlit as st
from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang

st.set_page_config(page_title="EnerTec – Wasserstoff-Versuchskoffer", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

# Gemeinsame Sprachwahl aus language.py (Standard DE; auf Startseite änderbar).
# Die gleiche Bilddatei wird für beide Sprachen verwendet.
BILD = Path("img/h2.png")

st.title(lang("Aufbau des Wasserstoff-Versuchskoffers", "Setting up the Hydrogen Experiment Kit"))
st.write(lang(
    "Auf dieser Seite lernt ihr die sieben wichtigsten Bestandteile unseres "
    "Wasserstoff-Versuchskoffers kennen. Die Nummern entsprechen den Markierungen "
    "im Foto. Lest die Hinweise durch, bevor ihr mit den Experimenten beginnt.",
    "On this page, you will get to know the seven main components of our hydrogen "
    "experiment kit. The numbers match the labels in the photo. Read the instructions "
    "before starting your experiments."
))

if BILD.is_file():
    st.image(
        str(BILD),
        caption=lang(
            "Wasserstoff-Versuchskoffer mit sieben nummerierten Komponenten",
            "Hydrogen experiment kit with seven numbered components"
        ),
        use_container_width=True,
    )
else:
    st.warning(lang(f"Das Aufbaubild fehlt noch: {BILD}", f"Setup image not found: {BILD}"))

st.subheader(lang("Die sieben Geräte auf einen Blick", "The seven components at a glance"))

geraete = [
    ("1", lang("Elektrolyseur", "Electrolyser"), lang(
        "Euer Molekülspalter: Macht aus Wasser mithilfe von Strom Wasserstoff und Sauerstoff.",
        "Your molecule splitter: Uses electricity to split water into hydrogen and oxygen."
    )),
    ("2", lang("Gasspeicher", "Gas storage unit"), lang(
        "Euer Gaslager: Sammelt die Gase und zeigt euch die erzeugten Volumina an.",
        "Your gas storage unit: Collects the gases and shows the volumes produced."
    )),
    ("3", lang("Brennstoffzelle", "Fuel cell"), lang(
        "Euer Stromerzeuger: Wandelt Wasserstoff und Sauerstoff wieder in Wasser und elektrische Energie um.",
        "Your power generator: Converts hydrogen and oxygen back into water, producing electrical energy."
    )),
    ("4", lang("Regulator", "Current regulator"), lang(
        "Euer Stromregler: Versorgt den Elektrolyseur kontrolliert mit elektrischem Strom.",
        "Your current controller: Supplies a controlled electric current to the electrolyser."
    )),
    ("5", lang("Multimeter", "Multimeter"), lang(
        "Euer Messgerät: Misst Spannung (V) oder Stromstärke (A).",
        "Your measuring instrument: Measures voltage (V) or electric current (A)."
    )),
    ("6", lang("Last", "Load"), lang(
        "Euer Verbraucher: Nutzt die erzeugte elektrische Energie, z. B. mit einer Lampe oder einem Motor.",
        "Your electrical load: Uses the generated electricity, e.g. to power a lamp or a motor."
    )),
    ("7", lang("Timer", "Timer"), lang(
        "Eure Stoppuhr: Misst, wie lange die Vorgänge dauern.",
        "Your stopwatch: Measures how long the processes take."
    )),
]

for nummer, name, kurztext in geraete:
    st.markdown(f"**{nummer} – {name}:** {kurztext}")

st.divider()
st.subheader(lang("Die Geräte im Detail", "The components in detail"))

st.markdown(lang(
    "### 1 – Elektrolyseur: Euer Molekülspalter",
    "### 1 – Electrolyser: Your molecule splitter"
))
st.write(lang(
    "Der Elektrolyseur nutzt elektrische Energie, um Wasser (H₂O) in Wasserstoff (H₂) "
    "und Sauerstoff (O₂) zu zerlegen. Er erzeugt also **Wasserstoff aus Wasser und Strom** "
    "– nicht umgekehrt.",
    "The electrolyser uses electrical energy to split water (H₂O) into hydrogen (H₂) "
    "and oxygen (O₂). In other words, it **produces hydrogen using water and electricity** "
    "– not the other way around."
))
st.write(lang(
    "Kontrolliert vor dem Versuch zusammen mit der Betreuungsperson den Wasserstand "
    "in den dafür vorgesehenen Kammern. Verwendet nur das für euren Versuchskoffer "
    "vorgesehene destillierte Wasser und schaut vor dem Versuch, ob der Füllstand "
    "an der Fülllinie steht. Verbindet die mit **H₂** und **O₂** gekennzeichneten "
    "Gasanschlüsse über die passenden Schläuche mit den entsprechenden Anschlüssen "
    "des Gasspeichers (2). Die Schläuche sollen fest sitzen.",
    "Before the experiment, check the water level in the designated chambers together "
    "with a supervisor. Only use the distilled water specified for your experiment kit, "
    "and make sure the water reaches the fill line. Connect the gas ports labelled "
    "**H₂** and **O₂** to the matching ports on the gas storage unit (2), using the "
    "appropriate tubing. Make sure the tubes fit securely."
))
st.info(lang(
    "Für die Versuche 1, 2 und 3 benötigt ihr den Elektrolyseur zur Wasserstofferzeugung.",
    "You will use the electrolyser to produce hydrogen in Experiments 1, 2 and 3."
))

st.markdown(lang(
    "### 2 – Gasspeicher: Euer Gaslager",
    "### 2 – Gas storage unit: Your gas reservoir"
))
st.write(lang(
    "Die beiden Messzylinder in der Mitte gehören zusammen und bilden **einen Gasspeicher**: "
    "Ein Teil sammelt Wasserstoff, der andere Sauerstoff. An der Skala könnt ihr ablesen, "
    "wie viel Gas entstanden ist. Bei der Wasserelektrolyse entsteht ungefähr doppelt "
    "so viel Wasserstoff wie Sauerstoff (Volumenverhältnis 2:1).",
    "The two measuring cylinders in the centre belong together and form **one gas storage "
    "unit**: One side collects hydrogen, the other oxygen. The scales show how much gas "
    "has been produced. Water electrolysis produces approximately twice as much hydrogen "
    "as oxygen by volume (a 2:1 volume ratio)."
))
st.write(lang(
    "Verbindet zunächst die Gasspeicher-Anschlüsse für H₂ und O₂ mit den gleichnamigen "
    "Anschlüssen des Elektrolyseurs. Vor jeder Messreihe prüft ihr mit der Betreuungsperson "
    "den vorgesehenen Wasserstand und den **Ausgangswert der Volumenskala**. Die Wassersäulen "
    "müssen in der korrekten Füllposition stehen. Notiert vor und nach einer Messung das "
    "jeweilige Wasserstoffvolumen.",
    "First, connect the H₂ and O₂ ports of the gas storage unit to the corresponding "
    "ports on the electrolyser. Before each series of measurements, check the specified "
    "water level and **initial reading on the volume scale** with a supervisor. The water "
    "columns must be in the correct starting position. Record the hydrogen volume before "
    "and after each measurement."
))
st.info(lang(
    "Besonders wichtig in Versuch 2 (Volumenänderung) und Versuch 3 (10 ml H₂ erzeugen).",
    "Especially important in Experiment 2 (change in volume) and Experiment 3 "
    "(producing 10 mL of H₂)."
))

st.markdown(lang(
    "### 3 – Brennstoffzelle: Euer Stromerzeuger",
    "### 3 – Fuel cell: Your power generator"
))
st.write(lang(
    "Die Brennstoffzelle arbeitet gewissermaßen umgekehrt zum Elektrolyseur: Sie "
    "verwendet Wasserstoff und Sauerstoff, um Wasser zu bilden. Dabei wird elektrische "
    "Energie frei, mit der sich eine Last (6) betreiben lässt.",
    "The fuel cell essentially works in the opposite direction to the electrolyser: "
    "It combines hydrogen and oxygen to form water. This process produces electrical "
    "energy that can be used to power a load (6)."
))
st.write(lang(
    "Die Brennstoffzelle wird über die vorgesehenen Gasanschlüsse mit dem Gasspeicher "
    "verbunden. Vor dem Betrieb kann es notwendig sein, eingeschlossene Luft aus den "
    "Gaswegen zu entfernen. **Lasst euch das Entlüften unbedingt von der Betreuungsperson "
    "zeigen, wenn ihr nicht damit vertraut seid.**",
    "Connect the fuel cell to the gas storage unit via the designated gas ports. "
    "Before operation, it may be necessary to remove trapped air from the gas lines. "
    "**If you are unfamiliar with this procedure, ask a supervisor to demonstrate "
    "how to purge the gas lines.**"
))
st.info(lang(
    "Die Brennstoffzelle ist insbesondere für Versuch 4 und die Wirkungsgrad-Auswertung "
    "in Versuch 5 relevant.",
    "The fuel cell is especially relevant to Experiment 4 and the efficiency evaluation "
    "in Experiment 5."
))

st.markdown(lang(
    "### 4 – Regulator: Euer Stromregler",
    "### 4 – Regulator: Your current controller"
))
st.write(lang(
    "Der Regulator ist die einstellbare elektrische Versorgung des Elektrolyseurs. "
    "Mit ihm legt ihr die Stromstärke für eure Messung fest. Stellt den Strom vor "
    "dem Anschließen auf den vorgesehenen Ausgangswert und schaltet erst nach "
    "Kontrolle des Aufbaus ein.",
    "The regulator is the adjustable electrical power supply for the electrolyser. "
    "Use it to set the current for your measurements. Set the current to the "
    "specified starting value before connecting the equipment and switch on "
    "only after the setup has been checked."
))
st.write(lang(
    "In Versuch 1 wird die Stromstärke von **0 bis 500 mA in Schritten von 50 mA** "
    "verändert. In Versuch 2 verwendet ihr **300, 400 und 500 mA**, und in Versuch 3 "
    "arbeitet ihr mit **konstant 400 mA**. Achtet immer auf die vom Gerät und "
    "der Betreuung vorgegebenen Grenzwerte – der Regler darf nicht beliebig "
    "hochgedreht werden.",
    "In Experiment 1, you vary the current from **0 to 500 mA in steps of 50 mA**. "
    "In Experiment 2, you use **300, 400 and 500 mA**, and in Experiment 3, "
    "you work at a **constant 400 mA**. Always observe the limits specified for "
    "the equipment and by your supervisor – do not increase the current arbitrarily."
))

st.markdown(lang(
    "### 5 – Multimeter: Euer Messgerät",
    "### 5 – Multimeter: Your measuring instrument"
))
st.write(lang(
    "Mit dem Digitalmultimeter könnt ihr die **Spannung U** in Volt (V) oder "
    "Millivolt (mV) und die **Stromstärke I** in Ampere (A) oder Milliampere (mA) messen. "
    "Dafür müsst ihr die richtigen Buchsen und den passenden Messbereich auswählen.",
    "The digital multimeter measures **voltage U** in volts (V) or millivolts (mV), "
    "and **current I** in amperes (A) or milliamperes (mA). "
    "You must select the correct sockets and measurement range."
))
st.write(lang(
    "Für eine **Spannungsmessung (DC V)** wird das Multimeter parallel zum zu messenden "
    "Bauteil angeschlossen. Für eine **Strommessung (DC A)** muss es in Reihe in den "
    "Stromkreis eingefügt werden. Die schwarze Messleitung kommt in der Regel in COM; "
    "die rote Leitung gehört in die zur Messart und Stromstärke passende Buchse. "
    "Beachtet unbedingt die Beschriftung eures konkreten Messgeräts.",
    "To measure **voltage (DC V)**, connect the multimeter in parallel with the component. "
    "To measure **current (DC A)**, connect it in series in the circuit. Usually, "
    "the black probe goes into COM, while the red probe goes into the socket "
    "appropriate for the measurement and current range. Always check the markings "
    "on your particular multimeter."
))
st.warning(lang(
    "Niemals das Multimeter in der Strommess-Einstellung direkt parallel an eine "
    "Spannungsquelle anschließen! Falls ihr unsicher seid, fragt die Betreuung.",
    "Never connect a multimeter set to current measurement directly across a voltage "
    "source! Ask a supervisor if you are unsure."
))

st.markdown(lang(
    "### 6 – Last: Euer elektrischer Verbraucher",
    "### 6 – Load: Your electrical consumer"
))
st.write(lang(
    "Die Last nimmt die von der Brennstoffzelle bereitgestellte elektrische Energie auf. "
    "Je nach Ausstattung des Versuchskoffers kann dies eine Lampe, eine LED oder ein "
    "kleiner Motor sein. So könnt ihr beobachten, dass aus Wasserstoff wieder "
    "nutzbare elektrische Energie wird.",
    "The load uses the electrical energy supplied by the fuel cell. Depending on the "
    "equipment in your kit, this may be a lamp, an LED or a small motor. This lets "
    "you see how hydrogen can be converted back into useful electrical energy."
))
st.write(lang(
    "Schließt eine Last nur entsprechend der Versuchsaufgabe und der "
    "Gerätekennzeichnung an. Prüft mit der Betreuungsperson, welcher Verbraucher "
    "für euren Versuch geeignet ist. Für manche Messungen wird statt einer Last "
    "das Multimeter benötigt.",
    "Only connect a load as specified in the experiment instructions and on the "
    "equipment labels. Ask your supervisor which load is suitable for your experiment. "
    "For some measurements, you will need the multimeter instead of a load."
))

st.markdown(lang(
    "### 7 – Timer: Eure Stoppuhr",
    "### 7 – Timer: Your stopwatch"
))
st.write(lang(
    "Mit dem Timer messt ihr, wie viel Zeit beim Experiment verstreicht. "
    "Das ist wichtig, um Messungen miteinander vergleichen zu können. "
    "In Versuch 2 dauert jede Messperiode **3 Minuten**. In Versuch 3 "
    "messt ihr die Zeit, die zur Erzeugung von **10 ml Wasserstoff** benötigt wird.",
    "Use the timer to measure how much time passes during an experiment. "
    "This is important for comparing measurements. In Experiment 2, each "
    "measurement period lasts **3 minutes**. In Experiment 3, you measure "
    "how long it takes to produce **10 mL of hydrogen**."
))
st.write(lang(
    "Startet den Timer immer am festgelegten Messbeginn und stoppt ihn am "
    "passenden Endpunkt. Notiert die Zeit in **Sekunden (s)**, wenn ihr "
    "anschließend die elektrische Energie mit E = U · I · t berechnen wollt.",
    "Always start the timer at the specified beginning of the measurement and stop "
    "it at the appropriate endpoint. Record the time in **seconds (s)** if you "
    "want to calculate the electrical energy using E = U · I · t."
))

st.divider()
st.subheader(lang("Vor dem Experiment: kurzer Aufbau-Check", "Before the experiment: Setup checklist"))

checkpunkte = [
    (
        "Destilliertes Wasser in den Gasspeicher eingefüllt und Füllstand gecheckt",
        "Distilled water filled into the gas storage unit and water level checked"
    ),
    (
        "Destilliertes Wasser in beide Kammern des Elektrolyseurs eingefüllt bis zur Kennlinie",
        "Both chambers of the electrolyzer filled with distilled water up to the marked fill line"
    ),
    (
        "Schläuche zwischen Elektrolyseur und Gasspeicher angeschlossen. Kontrolliert, ob alle Stopfen auf den nicht verwendeten Ausgängen sitzen",
        "Tubes connected between the electrolyzer and gas storage unit. Checked that all unused outlets are securely closed with plugs"
    ),
    (
        "Batterie in den Timer eingesetzt und Timer bereitgelegt",
        "Battery inserted into the timer and timer ready for use"
    ),
    (
        "Multimeter auf den richtigen Messbereich und die richtige Einheit eingestellt und gemäß Versuchsbeschreibung korrekt angeschlossen",
        "Multimeter set to the correct measurement range and unit, and connected correctly according to the experiment instructions"
    ),
    (
        "Bei Verwendung der Brennstoffzelle: Brennstoffzelle beim Anschließen entlüftet",
        "When using the fuel cell: Fuel cell purged during connection"
    ),
]

# Feste Keys: Der Hakenstatus bleibt beim Wechsel DE/EN erhalten.
for i, (de, en) in enumerate(checkpunkte):
    st.checkbox(lang(de, en), key=f"h2_aufbau_check_{i}")

st.warning(lang(
    "**Sicherheit:** Bei der Elektrolyse entsteht Wasserstoff, ein leicht entzündliches Gas. "
    "Arbeitet deshalb nur unter Aufsicht und haltet offene Flammen sowie Funkenquellen fern. "
    "Auch kleine Wasserstoffmengen können beim Entzünden gefährlich sein. "
    "Experimente mit offenen Flammen sind verboten. Beachtet die Anleitung des "
    "Versuchskoffers. Bei undichten Verbindungen oder ungewöhnlichem Verhalten "
    "den Versuch stoppen und die Betreuung informieren.",
    "**Safety:** Electrolysis produces hydrogen, a highly flammable gas. "
    "Work only under supervision and keep away from open flames and sources of sparks. "
    "Even small amounts of hydrogen can be dangerous if ignited. "
    "Experiments involving open flames are prohibited. Follow the instructions "
    "for your experiment kit. If you notice leaks or unusual behaviour, stop "
    "the experiment and inform a supervisor."
))
