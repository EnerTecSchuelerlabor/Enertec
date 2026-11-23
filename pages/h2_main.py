"""EnerTec – zweisprachige Übersicht der Wasserstoffexperimente."""
from pathlib import Path

import streamlit as st
from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang

st.set_page_config(page_title="EnerTec – Wasserstoff / Hydrogen", layout="wide")

hide_default_sidebar_nav()
h2_sidebar()

# Logo-Pfade aus dem bestehenden Projekt.
LOGO_STIFTUNG = "Solar/Logo_Stiftung_ohne_Hintergrund.png"
LOGO_ENERTEC = "Solar/Logo_EnerTec_ohne_Hintergrund.png"
LOGO_AES = "Solar/Logo_AES_ohne_Hintergrund.png"

if Path(LOGO_ENERTEC).is_file():
    st.logo(LOGO_ENERTEC)

col1, col2, col3 = st.columns(3)
for spalte, bild, beschreibung_de, beschreibung_en in [
    (col1, LOGO_STIFTUNG, "Stiftung", "Foundation"),
    (col2, LOGO_ENERTEC, "EnerTec", "EnerTec"),
    (col3, LOGO_AES, "Lehrstuhl AES", "AES Department"),
]:
    with spalte:
        if Path(bild).is_file():
            st.image(bild, width=250)
        else:
            st.caption(lang(
                f"Logo {beschreibung_de} nicht gefunden: {bild}",
                f"Logo {beschreibung_en} not found: {bild}",
            ))

st.title(lang("Übersicht – Wasserstoffexperimente", "Overview – Hydrogen experiments"))

st.subheader(lang("Bitte lesen!", "Please read!"))
st.write(lang(
    "Herzlich willkommen beim EnerTec Workshop!",
    "Welcome to the EnerTec Workshop!",
))
st.write(lang(
    "Ihr befindet euch auf der Startseite des Wasserstoff-Workshops. "
    "Hier lernt ihr, wie mithilfe von elektrischem Strom Wasserstoff erzeugt wird, "
    "wie eine Brennstoffzelle daraus wieder elektrische Energie gewinnt und "
    "welche Energieverluste dabei entstehen.",
    "You are on the main page of the hydrogen workshop. "
    "Here you will learn how electricity is used to produce hydrogen, "
    "how a fuel cell converts it back into electrical energy, "
    "and where energy losses occur in the process.",
))
st.write(lang(
    "Diese Website ist interaktiv aufgebaut. Über die Seitenleiste links könnt ihr "
    "zwischen den Versuchen und den Zusatzinformationen wechseln. "
    "Weiter unten findet ihr eine kurze Beschreibung aller fünf Versuche. "
    "Mit den Schaltflächen gelangt ihr direkt zu den jeweiligen Experimenten.",
    "This website is interactive. Use the sidebar on the left to switch "
    "between experiments and additional information. "
    "Below you will find a short description of all five experiments. "
    "Use the buttons to go directly to each experiment.",
))
st.write(lang(
    "Auf der Seite **Aufbau Versuchskoffer** findet ihr zusätzliche Hilfe zum Versuchsaufbau. "
    "Auch auf den einzelnen Versuchsseiten sind Aufbauhinweise vorhanden. "
    "Bei Fragen helfen euch die Betreuer vor Ort gerne weiter. Viel Spaß beim Experimentieren!",
    "The **Experiment kit setup** page provides additional help with assembling the equipment. "
    "You will also find setup instructions on the individual experiment pages. "
    "If you have any questions, the workshop supervisors will be happy to help. "
    "Have fun experimenting!",
))

st.info(lang(
    "**Wichtig:** Arbeitet mit den elektrischen Geräten und dem Wasserstoff-Versuchskoffer "
    "nur nach Einweisung durch eure Betreuer. Beachtet die Hinweise zum Versuchsaufbau.",
    "**Important:** Only use the electrical devices and hydrogen experiment kit "
    "after receiving instructions from your workshop supervisors. "
    "Follow the equipment setup instructions.",
))

st.divider()
st.subheader(lang("Übersicht der Versuche", "Overview of the experiments"))
st.write(lang(
    "Die Versuche bauen inhaltlich aufeinander auf. Ihr könnt sie über die Buttons direkt öffnen.",
    "The experiments build on one another. You can open each one directly using the buttons.",
))

# Jeder Eintrag: deutscher Titel, englischer Titel, deutsche Beschreibung,
# englische Beschreibung, Seitenpfad. Die Seitenpfade bleiben unverändert.
VERSUCHE = [
    (
        "Versuch 1: Zersetzungsspannung und I-U-Kennlinie",
        "Experiment 1: Decomposition voltage and I–V characteristic",
        "Ihr messt die Spannung am Elektrolyseur bei Stromstärken von 0 bis 500 mA. "
        "Aus euren Messwerten erstellt ihr eine I-U-Kennlinie und bestimmt näherungsweise "
        "die Zersetzungsspannung.",
        "You measure the voltage across the electrolyzer at currents from 0 to 500 mA. "
        "Using your measurements, you plot an I–V characteristic and estimate "
        "the decomposition voltage.",
        "pages/h2_Versuch_1.py",
    ),
    (
        "Versuch 2: Proportionalitätskonstante",
        "Experiment 2: Proportionality constant",
        "Ihr untersucht, wie viel Wasserstoff bei verschiedenen Stromstärken in jeweils "
        "drei Minuten entsteht. Aus der Volumenänderung berechnet ihr eine "
        "Proportionalitätskonstante.",
        "You investigate how much hydrogen is produced at different currents over "
        "three minutes each. From the change in volume, you calculate a "
        "proportionality constant.",
        "pages/h2_Versuch_2.py",
    ),
    (
        "Versuch 3: Zugeführte Energie des Elektrolyseurs",
        "Experiment 3: Electrical energy supplied to the electrolyzer",
        "Ihr erzeugt bei einer konstanten Stromstärke von 400 mA insgesamt 10 ml Wasserstoff. "
        "Dazu messt ihr die benötigte Zeit und Spannung und berechnet die zugeführte "
        "elektrische Energie.",
        "You produce a total of 10 ml of hydrogen at a constant current of 400 mA. "
        "You measure the time and voltage required and calculate the electrical energy supplied.",
        "pages/h2_Versuch_3.py",
    ),
    (
        "Versuch 4: Abgegebene Energie der Brennstoffzelle",
        "Experiment 4: Electrical energy delivered by the fuel cell",
        "Anhand vorgegebener Spannungs- und Stromwerte berechnet ihr, wie viel "
        "elektrische Energie die Brennstoffzelle abgibt. Danach könnt ihr eure "
        "Ergebnisse mit einer Musterlösung vergleichen.",
        "Using given voltage and current measurements, you calculate how much "
        "electrical energy the fuel cell delivers. You can then compare your "
        "results with a model solution.",
        "pages/h2_Versuch_4.py",
    ),
    (
        "Versuch 5: Wirkungsgrade",
        "Experiment 5: Efficiencies",
        "Ihr vergleicht die elektrische Energie aus den Versuchen 3 und 4 mit dem "
        "Energieinhalt des Wasserstoffs. So bestimmt ihr die Wirkungsgrade von "
        "Elektrolyseur, Brennstoffzelle und Gesamtsystem.",
        "You compare the electrical energy from experiments 3 and 4 with the "
        "energy stored in the hydrogen. This allows you to calculate the efficiencies "
        "of the electrolyzer, the fuel cell, and the overall system.",
        "pages/h2_Versuch_5.py",
    ),
]

for nummer, (titel_de, titel_en, beschreibung_de, beschreibung_en, seite) in enumerate(VERSUCHE, start=1):
    st.markdown(f"### {lang(titel_de, titel_en)}")
    st.write(lang(beschreibung_de, beschreibung_en))
    if st.button(
        lang(f"Zu Versuch {nummer}", f"Go to experiment {nummer}"),
        key=f"h2_uebersicht_versuch_{nummer}",
    ):
        st.switch_page(seite)
    st.divider()

st.subheader(lang("Zusatzinformationen", "Additional information"))
st.write(lang(
    "Weitere Erklärungen, Aufbauhilfen und Videos findet ihr über die Seitenleiste links. "
    "Wenn ihr bei der Durchführung nicht weiterkommt, fragt eure Betreuer.",
    "More explanations, setup instructions, and videos can be found in the sidebar on the left. "
    "If you need help during an experiment, ask your workshop supervisors.",
))

if st.button(
    lang("← Zurück zur Startseite", "← Back to the home page"),
    key="h2_uebersicht_startseite",
):
    st.switch_page("Startseite.py")
