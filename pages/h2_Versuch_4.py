"""EnerTec – Wasserstoff-Versuch 4 / Hydrogen Experiment 4."""

import pandas as pd
import streamlit as st

from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang, get_language


st.set_page_config(page_title="EnerTec – Wasserstoff / Hydrogen – Experiment 4", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

st.title(lang(
    "Versuch 4: Abgegebene Energie der Brennstoffzelle",
    "Experiment 4: Electrical energy delivered by the fuel cell",
))
st.write(lang(
    "In diesem Versuch berechnet ihr die elektrische Energie, die eine "
    "Brennstoffzelle bei der Nutzung von Wasserstoff abgibt. "
    "Füllt zunächst die Tabellen selbst aus und vergleicht eure Antworten "
    "danach mit der Musterlösung.",
    "In this experiment, you calculate the electrical energy delivered "
    "by a fuel cell using hydrogen. First complete the tables yourselves, "
    "then compare your answers with the model solution.",
))
st.divider()

st.subheader(lang("Information", "Information"))
st.write(lang(
    "Eine Brennstoffzelle ist ein technisches Gerät, in dem chemische "
    "Reaktionsenergie in Form elektrischer Energie freigesetzt wird. "
    "Dabei wird ein Brennstoff durch ein Oxidationsmittel oxidiert. "
    "In unserem Fall ist Wasserstoff der Brennstoff und Sauerstoff das "
    "Oxidationsmittel. In diesem Experiment ermittelt ihr die Grundlage "
    "für die Berechnung des Wirkungsgrades der Brennstoffzelle, "
    "der in Versuch 5 bestimmt wird.",
    "A fuel cell is a device that converts chemical reaction energy "
    "into electrical energy. In the process, a fuel reacts with an oxidizing "
    "agent. In our case, hydrogen is the fuel and oxygen is the oxidizing "
    "agent. In this experiment, you determine the data needed to calculate "
    "the fuel cell's efficiency in Experiment 5.",
))
st.divider()

st.subheader(lang("Aufgabe", "Task"))
st.write(lang(
    "Experiment 4 sorgt häufig für Probleme. Deshalb sind die Messwerte "
    "in der Versuchsvorlage bereits vorgegeben. Hier könnt ihr sie zuerst "
    "**selbst eintragen**, die Mittelwerte bestimmen und anschließend "
    "die abgegebene elektrische Energie berechnen. "
    "Die Musterlösung wird erst angezeigt, wenn ihr sie aufruft.",
    "Experiment 4 can be challenging. That is why the measured values "
    "are already provided in the worksheet. First **enter the values yourselves**, "
    "calculate the averages, and then calculate the electrical energy delivered. "
    "The model solution is only displayed when you choose to reveal it.",
))
st.info(lang(
    "**Formel:** E = I · U · t  \n\n"
    "Stromstärke **I** in A, Spannung **U** in V, Zeit **t** in s, "
    "Energie **E** in J.  \n\n"
    "Für **10 ml H₂** wird in dieser Aufgabe die berechnete Energie "
    "für **5 ml H₂** verdoppelt.",
    "**Formula:** E = I · U · t  \n\n"
    "Current **I** in A, voltage **U** in V, time **t** in s, "
    "energy **E** in J.  \n\n"
    "For **10 mL of H₂**, this task assumes twice the energy "
    "calculated for **5 mL of H₂**.",
))
st.divider()

st.subheader(lang("1. Messwerttabelle ausfüllen", "1. Complete the measurement table"))
st.write(lang(
    "Tragt zunächst die sechs Spannungs- und Stromwerte für die "
    "Wasserstoffvolumina von **0 bis 5 ml** ein. "
    "Berechnet anschließend die beiden Mittelwerte.",
    "First enter the six voltage and current values for hydrogen "
    "volumes from **0 to 5 mL**. Then calculate both averages.",
))

volumina = (0, 1, 2, 3, 4, 5)
loesung_spannung = (0.82, 0.83, 0.81, 0.82, 0.81, 0.83)
loesung_strom = (0.0621, 0.0623, 0.0616, 0.0630, 0.0627, 0.0625)

spaltenkopf = st.columns([1.1, 1.5, 1.6])
spaltenkopf[0].markdown(f"**{lang('Volumen H₂ (ml)', 'H₂ volume (mL)')}**")
spaltenkopf[1].markdown(f"**{lang('Spannung U (V)', 'Voltage U (V)')}**")
spaltenkopf[2].markdown(f"**{lang('Stromstärke I (A)', 'Current I (A)')}**")

messungen_u = []
messungen_i = []
for volumen in volumina:
    spalten = st.columns([1.1, 1.5, 1.6], vertical_alignment="center")
    spalten[0].write(f"**{volumen}**")
    with spalten[1]:
        u = st.number_input(
            lang(f"Spannung bei {volumen} ml (V)", f"Voltage at {volumen} mL (V)"),
            min_value=0.0,
            value=None,
            step=0.01,
            format="%.2f",
            key=f"h2_v4_u_{volumen}",
            placeholder=lang("U eingeben", "Enter U"),
            label_visibility="collapsed",
        )
    with spalten[2]:
        i = st.number_input(
            lang(f"Strom bei {volumen} ml (A)", f"Current at {volumen} mL (A)"),
            min_value=0.0,
            value=None,
            step=0.0001,
            format="%.4f",
            key=f"h2_v4_i_{volumen}",
            placeholder=lang("I eingeben", "Enter I"),
            label_visibility="collapsed",
        )
    messungen_u.append(u)
    messungen_i.append(i)

st.markdown(f"**{lang('Eure berechneten Mittelwerte:', 'Your calculated averages:')}**")
col_u, col_i = st.columns(2)
with col_u:
    mittel_u = st.number_input(
        lang("Mittlere Spannung U (V)", "Average voltage U (V)"),
        min_value=0.0, value=None, step=0.01, format="%.2f",
        placeholder=lang("Mittelwert berechnen", "Calculate the average"),
        key="h2_v4_mittel_u",
    )
with col_i:
    mittel_i = st.number_input(
        lang("Mittlere Stromstärke I (A)", "Average current I (A)"),
        min_value=0.0, value=None, step=0.0001, format="%.4f",
        placeholder=lang("Mittelwert berechnen", "Calculate the average"),
        key="h2_v4_mittel_i",
    )

st.divider()
st.subheader(lang("2. Energie berechnen", "2. Calculate energy"))
st.write(lang(
    "Übernehmt eure Mittelwerte und verwendet die vorgegebene "
    "**Zeit von 400 s**, um die Energie für 5 ml H₂ zu berechnen. "
    "Berechnet danach die Energie für 10 ml H₂.",
    "Use your average values and the specified **time of 400 s** "
    "to calculate the energy for 5 mL of H₂. "
    "Then calculate the energy for 10 mL of H₂.",
))

col1, col2, col3 = st.columns(3)
with col1:
    rechnung_i = st.number_input(
        lang("Stromstärke I (A)", "Current I (A)"),
        min_value=0.0, value=None, step=0.0001, format="%.4f",
        key="h2_v4_rechnung_i",
        placeholder=lang("Mittelwert eintragen", "Enter average"),
    )
with col2:
    rechnung_u = st.number_input(
        lang("Spannung U (V)", "Voltage U (V)"),
        min_value=0.0, value=None, step=0.01, format="%.2f",
        key="h2_v4_rechnung_u",
        placeholder=lang("Mittelwert eintragen", "Enter average"),
    )
with col3:
    st.metric(lang("Zeit t", "Time t"), "400 s")

col4, col5 = st.columns(2)
with col4:
    energie_5 = st.number_input(
        lang("Energie E für 5 ml H₂ (J)", "Energy E for 5 mL H₂ (J)"),
        min_value=0.0, value=None, step=0.1, format="%.1f",
        key="h2_v4_energie_5",
        placeholder=lang("Selbst ausrechnen", "Calculate it yourself"),
    )
with col5:
    energie_10 = st.number_input(
        lang("Energie E für 10 ml H₂ (J)", "Energy E for 10 mL H₂ (J)"),
        min_value=0.0, value=None, step=0.1, format="%.1f",
        key="h2_v4_energie_10",
        placeholder=lang("Selbst ausrechnen", "Calculate it yourself"),
    )

st.divider()
st.subheader(lang("3. Mit der Musterlösung vergleichen", "3. Compare with the model solution"))
st.write(lang(
    "Wenn ihr eure Tabellen ausgefüllt habt, könnt ihr die Musterlösung "
    "einblenden und eure Ergebnisse vergleichen.",
    "Once you have completed your tables, you can reveal the model solution "
    "and compare your results.",
))

if "h2_v4_loesung_sichtbar" not in st.session_state:
    st.session_state["h2_v4_loesung_sichtbar"] = False

if st.button(
    lang("Musterlösung ausblenden", "Hide model solution")
    if st.session_state["h2_v4_loesung_sichtbar"]
    else lang("Musterlösung anzeigen", "Show model solution"),
    type="primary",
    key="h2_v4_loesung_toggle",
):
    st.session_state["h2_v4_loesung_sichtbar"] = not st.session_state["h2_v4_loesung_sichtbar"]

if st.session_state["h2_v4_loesung_sichtbar"]:
    st.markdown(f"#### {lang('Musterlösung: Messwerttabelle', 'Model solution: Measurement table')}")

    def format_wert(wert, stellen):
        text = f"{wert:.{stellen}f}"
        return text.replace(".", ",") if get_language() == "DE" else text

    loesung_tabelle = pd.DataFrame({
        lang("Volumen H₂ (ml)", "H₂ volume (mL)"): [*volumina, lang("Mittelwert", "Average")],
        lang("Spannung U (V)", "Voltage U (V)"): [
            *[format_wert(u, 2) for u in loesung_spannung], format_wert(0.82, 2)
        ],
        lang("Stromstärke I (A)", "Current I (A)"): [
            *[format_wert(i, 4) for i in loesung_strom], format_wert(0.0624, 4)
        ],
    })
    st.dataframe(loesung_tabelle, use_container_width=True, hide_index=True)

    st.markdown(f"#### {lang('Musterlösung: Energieberechnung', 'Model solution: Energy calculation')}")
    st.latex(r"E_{5\,\mathrm{ml}} = 0{,}0624\,\mathrm{A}\cdot 0{,}82\,\mathrm{V}\cdot 400\,\mathrm{s} \approx 20{,}5\,\mathrm{J}")
    st.latex(r"E_{10\,\mathrm{ml}} = 2 \cdot 20{,}5\,\mathrm{J} = 41{,}0\,\mathrm{J}")
    st.caption(lang(
        "Die Musterlösung verwendet gerundete Mittelwerte wie in der Versuchsvorlage.",
        "The model solution uses rounded averages, as in the experiment worksheet.",
    ))

    st.markdown(f"#### {lang('Vergleich eurer Ergebnisse', 'Comparison with your results')}")
    vergleich = [
        (lang("Mittlere Spannung", "Average voltage"), mittel_u, 0.82, 0.005, "V"),
        (lang("Mittlere Stromstärke", "Average current"), mittel_i, 0.0624, 0.00005, "A"),
        (lang("Stromstärke in der Rechnung", "Current used in the calculation"), rechnung_i, 0.0624, 0.00005, "A"),
        (lang("Spannung in der Rechnung", "Voltage used in the calculation"), rechnung_u, 0.82, 0.005, "V"),
        (lang("Energie für 5 ml", "Energy for 5 mL"), energie_5, 20.5, 0.05, "J"),
        (lang("Energie für 10 ml", "Energy for 10 mL"), energie_10, 41.0, 0.05, "J"),
    ]
    for name, eingabe, soll, toleranz, einheit in vergleich:
        soll_text = f"{soll:g}".replace(".", ",") if get_language() == "DE" else f"{soll:g}"
        if eingabe is None:
            st.write(lang(f"**{name}:** Noch nicht eingetragen.", f"**{name}:** Not entered yet."))
        elif abs(eingabe - soll) <= toleranz + 1e-10:
            st.success(lang(
                f"{name}: Stimmt mit der Musterlösung überein ({soll_text} {einheit}).",
                f"{name}: Matches the model solution ({soll_text} {einheit}).",
            ))
        else:
            st.warning(lang(
                f"{name}: Noch einmal prüfen (Musterlösung: {soll_text} {einheit}).",
                f"{name}: Please check again (model solution: {soll_text} {einheit}).",
            ))

    st.write(lang(
        "**Denkt daran:** Kleine Rundungsabweichungen sind je nach Rechenweg möglich.",
        "**Remember:** Small rounding differences are possible depending on the calculation method.",
    ))

st.divider()
st.subheader(lang("Frage zur Auswertung", "Evaluation question"))
st.write(lang(
    "Warum ist die abgegebene elektrische Energie der Brennstoffzelle "
    "für die spätere Berechnung des Wirkungsgrades wichtig?",
    "Why is the electrical energy delivered by the fuel cell "
    "important for calculating its efficiency later on?",
))
st.text_area(
    lang("Eure Überlegungen", "Your thoughts"),
    key="h2_v4_antwort",
    placeholder=lang("Schreibt hier eure Antwort ...", "Write your answer here ..."),
)
