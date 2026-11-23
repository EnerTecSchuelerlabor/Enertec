"""EnerTec – interaktives Wasserstoff-Quiz (Deutsch/Englisch).

Nur diese Datei nötig; die im EnerTec-Projekt vorhandenen Module
language.py und navigation.py werden wie auf den anderen Seiten verwendet.
"""

import streamlit as st
from language import lang
from navigation import hide_default_sidebar_nav, h2_sidebar

st.set_page_config(page_title="EnerTec – Wasserstoff-Quiz", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

# Jede Frage: (Frage DE, Frage EN, vier Antworten als (DE, EN), korrekte Position,
#             Erklärung DE, Erklärung EN). Korrekte Position beginnt bei 0.
FRAGEN = [
    (
        "Was macht ein Elektrolyseur?",
        "What does an electrolyzer do?",
        [("Er wandelt Wasserstoff direkt in Strom um.", "It converts hydrogen directly into electricity."),
         ("Er zerlegt Wasser mithilfe von Strom in Wasserstoff und Sauerstoff.", "It splits water into hydrogen and oxygen using electricity."),
         ("Er speichert elektrische Energie in einer Batterie.", "It stores electricity in a battery."),
         ("Er misst das Gasvolumen.", "It measures gas volume.")],
        1,
        "Bei der Elektrolyse wird Wasser durch elektrische Energie in H₂ und O₂ zerlegt.",
        "Electrolysis uses electrical energy to split water into H₂ and O₂.",
    ),
    (
        "Welche chemische Gleichung beschreibt die Wasserelektrolyse?",
        "Which chemical equation describes water electrolysis?",
        [("2 H₂O → 2 H₂ + O₂", "2 H₂O → 2 H₂ + O₂"),
         ("H₂ + O₂ → H₂O₂", "H₂ + O₂ → H₂O₂"),
         ("2 H₂ + O₂ → 2 H₂O", "2 H₂ + O₂ → 2 H₂O"),
         ("H₂O → H₂ + 2 O₂", "H₂O → H₂ + 2 O₂")],
        0,
        "Die ausgeglichene Reaktionsgleichung lautet 2 H₂O → 2 H₂ + O₂.",
        "The balanced equation is 2 H₂O → 2 H₂ + O₂.",
    ),
    (
        "In welchem Volumenverhältnis entstehen H₂ und O₂ bei gleicher Temperatur und gleichem Druck?",
        "What is the volume ratio of H₂ to O₂ at the same temperature and pressure?",
        [("1 : 1", "1 : 1"), ("1 : 2", "1 : 2"),
         ("2 : 1", "2 : 1"), ("3 : 1", "3 : 1")],
        2,
        "Aus zwei Wassermolekülen entstehen zwei H₂-Moleküle und ein O₂-Molekül: 2 : 1.",
        "Two water molecules produce two H₂ molecules and one O₂ molecule: 2 : 1.",
    ),
    (
        "Was bedeutet Zersetzungsspannung beim Elektrolyseur?",
        "What does decomposition voltage mean for an electrolyzer?",
        [("Die Spannung, die ein Timer benötigt.", "The voltage needed by a timer."),
         ("Die Spannung am Widerstand einer Lampe.", "The voltage across a lamp resistor."),
         ("Die stets konstante Spannung einer Brennstoffzelle.", "The always-constant voltage of a fuel cell."),
         ("Die Mindestspannung, ab der die gewünschte Elektrolysereaktion ablaufen kann.", "The minimum voltage from which the desired electrolysis reaction can proceed.")],
        3,
        "Die Zersetzungsspannung kennzeichnet die unter den jeweiligen Bedingungen benötigte Mindestspannung; praktisch können weitere Verluste hinzukommen.",
        "The decomposition voltage marks the minimum required under the given conditions; practical losses may require additional voltage.",
    ),
    (
        "Welche Größe misst ihr mit dem Multimeter bei der Einstellung DC A?",
        "What quantity does a multimeter measure when set to DC A?",
        [("Gleichstromstärke", "Direct current"),
         ("Gleichspannung", "Direct voltage"),
         ("Zeit", "Time"),
         ("Gasvolumen", "Gas volume")],
        0,
        "DC A steht für die Messung der Gleichstromstärke in Ampere.",
        "DC A measures direct current in amperes.",
    ),
    (
        "Wie wird ein Multimeter zur Spannungsmessung angeschlossen?",
        "How is a multimeter connected to measure voltage?",
        [("In Reihe zum Bauteil", "In series with the component"),
         ("Parallel zum Bauteil", "In parallel with the component"),
         ("Nur an den Timer", "Only to the timer"),
         ("An den Gasschlauch", "To the gas tube")],
        1,
        "Die Spannung wird zwischen zwei Punkten gemessen: Das Voltmeter liegt parallel.",
        "Voltage is measured between two points: the voltmeter is connected in parallel.",
    ),
    (
        "Welche Aufgabe hat die Brennstoffzelle?",
        "What is the purpose of the fuel cell?",
        [("Sie zerlegt Wasser mit zugeführtem Strom.", "It splits water using supplied electricity."),
         ("Sie erhöht das Gasvolumen durch Erwärmung.", "It increases gas volume by heating."),
         ("Sie erzeugt aus Wasserstoff und Sauerstoff elektrische Energie und Wasser.", "It generates electrical energy and water from hydrogen and oxygen."),
         ("Sie misst den Strom ohne Messgerät.", "It measures current without an instrument.")],
        2,
        "In der Brennstoffzelle reagieren H₂ und O₂ zu Wasser; dabei wird elektrische Energie bereitgestellt.",
        "In a fuel cell, H₂ and O₂ react to form water, supplying electrical energy.",
    ),
    (
        "Wie berechnet ihr die elektrische Energie bei konstanter Spannung und Stromstärke?",
        "How do you calculate electrical energy at constant voltage and current?",
        [("E = U / I", "E = U / I"),
         ("E = U + I + t", "E = U + I + t"),
         ("E = I / t", "E = I / t"),
         ("E = U · I · t", "E = U · I · t")],
        3,
        "Leistung P = U · I und Energie E = P · t, also E = U · I · t.",
        "Power P = U · I and energy E = P · t, so E = U · I · t.",
    ),
    (
        "Ein Elektrolyseur läuft bei 0,4 A und 2,0 V für 100 s. Wie viel elektrische Energie wird zugeführt?",
        "An electrolyzer runs at 0.4 A and 2.0 V for 100 s. How much electrical energy is supplied?",
        [("80 J", "80 J"), ("8 J", "8 J"),
         ("200 J", "200 J"), ("0,8 J", "0.8 J")],
        0,
        "E = U · I · t = 2,0 V · 0,4 A · 100 s = 80 J.",
        "E = U · I · t = 2.0 V · 0.4 A · 100 s = 80 J.",
    ),
    (
        "Warum ist der Wirkungsgrad eines realen Elektrolyseur-Brennstoffzellen-Systems kleiner als 100 %?",
        "Why is the efficiency of a real electrolyzer–fuel-cell system below 100%?",
        [("Weil beim Betrieb zusätzliche Energie aus dem Nichts entsteht.", "Because extra energy is created from nothing."),
         ("Weil bei den Umwandlungen beispielsweise Wärmeverluste auftreten.", "Because conversions involve losses, for example as heat."),
         ("Weil die Zeitmessung Energie erzeugt.", "Because measuring time generates energy."),
         ("Weil Wasser keinen Sauerstoff enthält.", "Because water contains no oxygen.")],
        1,
        "Bei jeder realen Umwandlung treten Verluste auf, etwa durch Wärmeentwicklung und elektrische Widerstände.",
        "Real energy conversions involve losses, such as heat and electrical resistance.",
    ),
]

# Session-State bleibt beim Wechsel zwischen Seiten und Sprachen erhalten.
INDEX_KEY = "h2_quiz_index"
ANTWORTEN_KEY = "h2_quiz_antworten"

if INDEX_KEY not in st.session_state:
    st.session_state[INDEX_KEY] = 0
if ANTWORTEN_KEY not in st.session_state:
    st.session_state[ANTWORTEN_KEY] = []


def neu_starten():
    st.session_state[INDEX_KEY] = 0
    st.session_state[ANTWORTEN_KEY] = []
    for i in range(len(FRAGEN)):
        st.session_state.pop(f"h2_quiz_auswahl_{i}", None)


st.title(lang("Wasserstoff-Quiz", "Hydrogen quiz"))
st.write(lang(
    "Testet euer Wissen zu Elektrolyse, Brennstoffzellen und den fünf Experimenten. "
    "Pro Frage gibt es vier Antworten, aber nur eine ist richtig.",
    "Test your knowledge of electrolysis, fuel cells and the five experiments. "
    "Each question has four answers, but only one is correct.",
))

index = st.session_state[INDEX_KEY]
antworten = st.session_state[ANTWORTEN_KEY]
gesamt = len(FRAGEN)

if index < gesamt:
    st.progress(index / gesamt)
    st.caption(lang(f"Frage {index + 1} von {gesamt}", f"Question {index + 1} of {gesamt}"))
    frage_de, frage_en, optionen, richtig, erklaerung_de, erklaerung_en = FRAGEN[index]
    st.subheader(lang(frage_de, frage_en))

    # Die interne Auswahl ist eine Zahl und bleibt deshalb auch bei Sprachwechsel gültig.
    auswahl = st.radio(
        lang("Wähle eine Antwort:", "Choose one answer:"),
        options=list(range(4)),
        format_func=lambda n: lang(optionen[n][0], optionen[n][1]),
        index=None,
        key=f"h2_quiz_auswahl_{index}",
    )

    if st.button(
        lang("Antwort bestätigen und weiter", "Submit answer and continue"),
        type="primary",
        disabled=auswahl is None,
        use_container_width=True,
    ):
        # Genau eine Antwort je Frage; bei jedem Weiterklick nur diese Frage bewerten.
        st.session_state[ANTWORTEN_KEY].append(auswahl == richtig)
        st.session_state[INDEX_KEY] += 1
        st.rerun()

    st.caption(lang(
        "Nach dem Bestätigen erscheint direkt die nächste Frage. Die Auswertung gibt es am Ende.",
        "After submitting, the next question appears. Your results are shown at the end.",
    ))
else:
    st.progress(1.0)
    richtig_anzahl = sum(antworten)
    falsch_anzahl = gesamt - richtig_anzahl
    st.success(lang("Quiz abgeschlossen!", "Quiz completed!"))
    st.subheader(lang("Dein Ergebnis", "Your result"))
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(lang("Richtig", "Correct"), richtig_anzahl)
    with col2:
        st.metric(lang("Falsch", "Incorrect"), falsch_anzahl)
    with col3:
        st.metric(lang("Erfolgsquote", "Score"), f"{richtig_anzahl / gesamt:.0%}")

    if richtig_anzahl == gesamt:
        st.balloons()
        st.write(lang("Super! Alle Fragen richtig beantwortet.", "Great! All answers are correct."))
    elif richtig_anzahl >= gesamt * 0.7:
        st.write(lang("Gut gemacht! Ihr kennt euch mit Wasserstoff schon gut aus.", "Well done! You already know a lot about hydrogen."))
    else:
        st.write(lang("Schaut euch die Erklärungsseite noch einmal an und versucht es erneut.", "Review the explanation page and try again."))

    if st.button(lang("Quiz erneut starten", "Restart quiz"), type="primary"):
        neu_starten()
        st.rerun()

st.divider()
if st.button(lang("Zur Erklärung Wasserstoff", "Back to hydrogen explanation")):
    st.switch_page("pages/h12_Erklärung_Wasserstoff.py")
