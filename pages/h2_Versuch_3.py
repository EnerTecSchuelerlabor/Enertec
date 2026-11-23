from pathlib import Path

import pandas as pd
import streamlit as st

from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang

st.set_page_config(page_title="EnerTec – Wasserstoff / Hydrogen – Experiment 3", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

st.title(lang("Versuch 3: Zugeführte Energie des Elektrolyseurs", "Experiment 3: Electrical energy supplied to the electrolyzer"))
st.write(lang(
    "In diesem Versuch messt ihr, wie viel elektrische Energie benötigt wird, "
    "um **10 ml Wasserstoff** mit dem Elektrolyseur zu erzeugen.",
    "In this experiment, you measure how much electrical energy is required "
    "to produce **10 mL of hydrogen** using the electrolyzer."
))
st.divider()

st.subheader(lang("Information", "Information"))
st.write(lang(
    "In den folgenden Experimenten beschäftigen wir uns mit dem **Wirkungsgrad**. "
    "Der Wirkungsgrad ist der Quotient aus abgegebener Leistung oder Energie "
    "und aufgenommener Leistung oder Energie. In diesem Versuch ermittelt ihr "
    "die Grundlage für die Berechnung des Wirkungsgrades des Elektrolyseurs, "
    "der in **Versuch 5** abschließend bestimmt wird.",
    "In the following experiments, you will study **efficiency**. "
    "Efficiency is the ratio of useful output power or energy to input power or energy. "
    "In this experiment, you collect the data required to calculate the efficiency "
    "of the electrolyzer, which you will determine in **Experiment 5**."
))
st.divider()

st.subheader(lang("Aufbau", "Setup"))
aufbau_bild = Path("img/h2_versuch1_aufbau.png")
if aufbau_bild.exists():
    st.image(
        str(aufbau_bild),
        caption=lang("Versuchsaufbau (wie bei Versuch 1)", "Experimental setup (as in Experiment 1)"),
        width=650,
    )
else:
    st.info(lang("Verwendet den Versuchsaufbau aus Versuch 1.", "Use the setup from Experiment 1."))
st.write(lang("**Digitalmultimeter Spannung:** DC V", "**Digital multimeter – voltage:** DC V"))
st.write(lang("**Digitalmultimeter Strom:** DC A", "**Digital multimeter – current:** DC A"))
st.divider()

st.subheader(lang("Aufgabe", "Task"))
st.write(lang(
    "Betreibt den Stromregler mit einer **konstanten Stromstärke von 400 mA**. "
    "Messt die Zeit, die benötigt wird, um **10 ml H₂** zu erzeugen. "
    "Notiert die gemessene Zeit und die Spannung während des Experiments.",
    "Operate the current regulator at a **constant current of 400 mA**. "
    "Measure the time needed to produce **10 mL of H₂**. "
    "Record the elapsed time and the voltage during the experiment."
))
st.write(lang(
    "Da die Spannung während des Versuchs ungefähr konstant sein sollte, "
    "empfiehlt es sich, sie mehrmals abzulesen: beispielsweise immer dann, "
    "wenn weitere **2 ml Wasserstoff** erzeugt wurden. "
    "Bildet anschließend den Mittelwert aus euren Spannungsmessungen.",
    "Since the voltage should remain approximately constant during the experiment, "
    "it is useful to read it several times, for example whenever another "
    "**2 mL of hydrogen** has been produced. "
    "Then calculate the mean of your voltage measurements."
))
st.write(lang(
    "Tragt die Messwerte in die digitale Tabelle ein. "
    "Die elektrische Energie zur Erzeugung von 10 ml Wasserstoff "
    "wird automatisch berechnet.",
    "Enter your measurements in the digital table. "
    "The electrical energy required to produce 10 mL of hydrogen "
    "will be calculated automatically."
))
st.info(lang(
    "**Formel:** E = I · U · t  \n\n"
    "Für die Berechnung gilt: Stromstärke I in **A**, "
    "Spannung U in **V**, Zeit t in **s**; Ergebnis E in **J**.",
    "**Formula:** E = I · U · t  \n\n"
    "For the calculation, use current I in **A**, "
    "voltage U in **V**, and time t in **s**; the result E is in **J**."
))
st.divider()

st.subheader(lang("Digitale Messwerttabelle", "Digital measurement table"))
st.caption(lang(
    "Messt die Spannung bei den angegebenen Wasserstoffvolumina. "
    "Noch nicht gemessene Werte können leer bleiben.",
    "Measure the voltage at the specified hydrogen volumes. "
    "You can leave values you have not measured yet blank."
))

VOLUMINA_ML = (0, 2, 4, 6, 8, 10)
STROM_A = 0.4

spannungen = []
spalten = st.columns(3)
for index, volumen in enumerate(VOLUMINA_ML):
    with spalten[index % 3]:
        spannung = st.number_input(
            lang(f"Spannung bei {volumen} ml H₂ (V)", f"Voltage at {volumen} mL H₂ (V)"),
            min_value=0.0,
            value=None,
            step=0.01,
            format="%.2f",
            placeholder=lang("Messwert eingeben", "Enter measured value"),
            key=f"h2_v3_spannung_{volumen}",
        )
        spannungen.append(spannung)

vorhandene_spannungen = [u for u in spannungen if u is not None]
mittelwert = (
    sum(vorhandene_spannungen) / len(vorhandene_spannungen)
    if vorhandene_spannungen else None
)

tabelle = pd.DataFrame({
    lang("Volumen H₂ (ml)", "H₂ volume (mL)"): [*VOLUMINA_ML, lang("Mittelwert", "Mean")],
    lang("Spannung U (V)", "Voltage U (V)"): [*spannungen, mittelwert],
})
st.dataframe(tabelle, use_container_width=True, hide_index=True)

st.divider()
st.subheader(lang("Berechnung der zugeführten elektrischen Energie", "Calculating the electrical energy supplied"))

zeit_s = st.number_input(
    lang("Benötigte Zeit für 10 ml H₂ (in Sekunden)", "Time required for 10 mL H₂ (in seconds)"),
    min_value=0.0,
    value=None,
    step=1.0,
    format="%.1f",
    placeholder=lang("Gemessene Zeit eingeben", "Enter measured time"),
    key="h2_v3_zeit_s",
)

energie_j = (
    STROM_A * mittelwert * zeit_s
    if mittelwert is not None and zeit_s is not None and zeit_s > 0
    else None
)

# Einheitliche Formatierung; die Ergebnisse und Eingaben bleiben beim Sprachwechsel erhalten.
def zahl(wert, stellen=2):
    if wert is None:
        return "–"
    ausgabe = f"{wert:.{stellen}f}"
    return ausgabe.replace(".", ",") if lang("DE", "EN") == "DE" else ausgabe

col_i, col_u, col_t, col_e = st.columns(4)
col_i.metric(lang("Strom I", "Current I"), f"{zahl(STROM_A, 1)} A")
col_u.metric(lang("Mittlere Spannung U", "Mean voltage U"), f"{zahl(mittelwert)} V" if mittelwert is not None else "–")
col_t.metric(lang("Zeit t", "Time t"), f"{zahl(zeit_s, 1)} s" if zeit_s is not None else "–")
col_e.metric(lang("Energie E", "Energy E"), f"{zahl(energie_j)} J" if energie_j is not None else "–")

if mittelwert is not None and zeit_s is not None and zeit_s > 0:
    st.success(f"E = {zahl(STROM_A, 1)} A · {zahl(mittelwert)} V · {zahl(zeit_s, 1)} s "
               f"= **{zahl(energie_j)} J**")
    if len(vorhandene_spannungen) < len(VOLUMINA_ML):
        st.warning(lang(
            "Es fehlen noch Spannungsmesswerte. Der angezeigte Mittelwert "
            "und die Energie basieren nur auf den bisher eingegebenen Spannungen.",
            "Some voltage measurements are still missing. The displayed mean "
            "and energy are based only on the voltages entered so far."
        ))
else:
    st.info(lang(
        "Tragt mindestens einen Spannungswert und die gemessene Zeit ein, "
        "damit die Energie berechnet werden kann. Für das vollständige "
        "Versuchsergebnis sollten alle sechs Spannungswerte vorliegen.",
        "Enter at least one voltage value and the measured time to calculate the energy. "
        "For a complete experimental result, all six voltage measurements should be available."
    ))

st.markdown(f"**{lang('Ergebnistabelle', 'Results table')}**")
ergebnis = pd.DataFrame([{
    lang("Stromstärke I (A)", "Current I (A)"): STROM_A,
    lang("Mittlere Spannung U (V)", "Mean voltage U (V)"): mittelwert,
    lang("Zeit t (s)", "Time t (s)"): zeit_s,
    lang("Energie E (J)", "Energy E (J)"): energie_j,
}])
st.dataframe(ergebnis, hide_index=True, use_container_width=True)

st.divider()
st.subheader(lang("Auswertung", "Evaluation"))
st.write(lang(
    "Vergleicht die sechs Spannungsmessungen: Ist die Spannung während der "
    "Wasserstofferzeugung tatsächlich annähernd konstant? "
    "Welche Bedeutung hat die mittlere Spannung für die Energieberechnung?",
    "Compare the six voltage measurements: Does the voltage really remain "
    "approximately constant during hydrogen production? "
    "Why is the mean voltage important for the energy calculation?"
))
st.text_area(
    lang("Eure Beobachtungen (optional)", "Your observations (optional)"),
    placeholder=lang("Notiert hier eure Beobachtungen ...", "Write your observations here ..."),
    key="h2_v3_beobachtung",
)
