"""EnerTec – Wasserstoffversuch 2 / Hydrogen experiment 2."""
from pathlib import Path

import pandas as pd
import streamlit as st

from language import lang
from navigation import hide_default_sidebar_nav, h2_sidebar

st.set_page_config(page_title="EnerTec – Wasserstoff / Hydrogen – Experiment 2", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

st.title(lang("Versuch 2: Proportionalitätskonstante", "Experiment 2: Proportionality constant"))
st.write(lang(
    "In diesem Versuch untersucht ihr, wie viel Wasserstoff ein Elektrolyseur "
    "bei verschiedenen Stromstärken innerhalb von drei Minuten erzeugt. "
    "Aus euren Messwerten berechnet ihr die Proportionalitätskonstante.",
    "In this experiment, you investigate how much hydrogen an electrolyzer produces "
    "at different currents over a period of three minutes. "
    "You use your measurements to calculate the proportionality constant."
))
st.divider()

st.subheader(lang("Information", "Information"))
st.write(lang(
    "Elektrolyseure werden zur gezielten Herstellung von Wasserstoff verwendet. "
    "Dabei wird der erzeugte Wasserstoff in der Regel nicht direkt verbraucht, "
    "sondern zunächst gespeichert. Nichtsdestotrotz ist eine gesteuerte "
    "Erzeugung eines bestimmten Volumens gewünscht. Dazu ist es notwendig, "
    "die erzeugte Menge an Gas für eine eingespeiste Menge an Energie zu kennen.",
    "Electrolyzers are used to produce hydrogen in a controlled way. "
    "The hydrogen produced is generally not consumed immediately but is stored first. "
    "Being able to produce a specific volume is therefore useful. This requires "
    "knowing how much gas is produced for a given amount of energy supplied."
))
st.write(lang(
    "Im ersten Schritt betrachten wir dazu vereinfacht die Stromstärke über "
    "der Zeit, um ein Maß für die erzeugte Menge an Wasserstoff zu gewinnen. "
    "Dieses Maß nennen wir **Proportionalitätskonstante**. Sie gibt an, "
    "wie viele Milliliter Wasserstoff pro Minute und pro Ampere "
    "vom Elektrolyseur erzeugt werden. Damit kann die erzeugte Menge "
    "Wasserstoff für verschiedene Zeiten und Stromstärken abgeschätzt werden.",
    "As a first step, we simplify this relationship by considering the current and "
    "measurement duration to determine how much hydrogen is produced. "
    "We call this measure the **proportionality constant**. It expresses how many "
    "millilitres of hydrogen the electrolyzer produces per minute per ampere. "
    "It can be used to estimate the amount of hydrogen produced at different "
    "currents and over different periods of time."
))
st.divider()

st.subheader(lang("Aufbau", "Setup"))
aufbau_bild = Path("img/h2_versuch1_aufbau.png")
if aufbau_bild.exists():
    st.image(str(aufbau_bild), caption=lang(
        "Versuchsaufbau (wie bei Versuch 1)", "Experimental setup (as in Experiment 1)"
    ), width=650)
else:
    st.info(lang(
        "Verwendet den Versuchsaufbau aus Versuch 1. Die Abbildung kann unter "
        "'img/h2_versuch1_aufbau.png' ergänzt werden.",
        "Use the setup from Experiment 1. The image can be added at "
        "'img/h2_versuch1_aufbau.png'."
    ))
st.write(lang("**Digitalmultimeter Strom:** DC A", "**Digital multimeter – current:** DC A"))
st.divider()

st.subheader(lang("Aufgabe", "Task"))
st.write(lang(
    "Bestimmt für verschiedene Stromstärken die **Volumenänderung des "
    "Wasserstoffs während einer Messdauer von jeweils drei Minuten**. "
    "Notiert das Wasserstoffvolumen zu Beginn und am Ende jeder Messperiode "
    "und berechnet daraus die Volumenänderung (Delta).",
    "For different currents, determine the **change in hydrogen volume during "
    "each three-minute measurement period**. Record the hydrogen volume at "
    "the beginning and end of each period and calculate the change (delta)."
))
st.write(lang(
    "Das Volumen zu Beginn der ersten Messung entspricht dem Volumen "
    "am Ende von Versuch 1, sofern ihr direkt mit diesem Aufbau weitermesst. "
    "Stellt danach nacheinander die vorgegebenen Stromstärken "
    "von **300 mA**, **400 mA** und **500 mA** ein.",
    "If you continue directly with the same setup, the starting volume of the "
    "first measurement corresponds to the final volume from Experiment 1. "
    "Then set the specified currents of **300 mA**, **400 mA**, and **500 mA** in turn."
))
st.write(lang(
    "Berechnet aus der Volumenänderung zuerst die Menge Wasserstoff "
    "in **ml pro Minute** und daraus die Proportionalitätskonstante "
    "in **ml/(min·A)**.",
    "First calculate the amount of hydrogen produced in **ml per minute** "
    "from the volume change, then determine the proportionality constant "
    "in **ml/(min·A)**."
))
st.info(lang(
    "**Hinweis:** Jede Messung dauert **3 Minuten**. "
    "Lest das Anfangs- und Endvolumen jeweils an derselben Skala ab. "
    "Tragt die gemessenen Volumina in **ml** ein.",
    "**Note:** Each measurement lasts **3 minutes**. Read the initial and "
    "final volumes using the same scale. Enter the measured volumes in **ml**."
))
st.divider()

st.subheader(lang("Digitale Messwerttabelle", "Digital measurement table"))
st.caption(lang(
    "Gebt für jede Stromstärke das Start- und Endvolumen ein. "
    "Die weiteren Spalten werden automatisch berechnet. Nicht gemessene Werte bleiben leer.",
    "Enter the starting and final volumes for each current. The remaining columns "
    "are calculated automatically. Values that have not been measured remain blank."
))

STROMSTAERKEN_MA = (300, 400, 500)
MESSDAUER_MIN = 3.0


def formatiere_wert(wert, stellen=2):
    if pd.isna(wert):
        return "–"
    text = f"{wert:.{stellen}f}"
    return text.replace(".", ",") if lang("DE", "EN") == "DE" else text


# Stabile interne Bezeichner; nur die sichtbaren Spaltenüberschriften werden übersetzt.
messungen = []
for strom_ma in STROMSTAERKEN_MA:
    st.markdown(lang(
        f"**Messung bei {strom_ma} mA – Messdauer: 3 Minuten**",
        f"**Measurement at {strom_ma} mA – duration: 3 minutes**"
    ))
    col_start, col_ende = st.columns(2)
    with col_start:
        start = st.number_input(
            lang(f"Volumen H₂ Start (ml) bei {strom_ma} mA",
                 f"Initial H₂ volume (ml) at {strom_ma} mA"),
            min_value=0.0, value=None, step=0.1, format="%.1f",
            placeholder=lang("Startvolumen eingeben", "Enter initial volume"),
            key=f"h2_v2_start_{strom_ma}",
        )
    with col_ende:
        ende = st.number_input(
            lang(f"Volumen H₂ Ende (ml) bei {strom_ma} mA",
                 f"Final H₂ volume (ml) at {strom_ma} mA"),
            min_value=0.0, value=None, step=0.1, format="%.1f",
            placeholder=lang("Endvolumen eingeben", "Enter final volume"),
            key=f"h2_v2_ende_{strom_ma}",
        )

    if start is not None and ende is not None and ende >= start:
        delta_drei_min = ende - start
        delta_pro_min = delta_drei_min / MESSDAUER_MIN
        konstante = delta_pro_min / (strom_ma / 1000.0)
    else:
        delta_drei_min = None
        delta_pro_min = None
        konstante = None
        if start is not None and ende is not None:
            st.warning(lang(
                f"Bei {strom_ma} mA ist das Endvolumen kleiner als das Startvolumen. "
                "Bitte überprüft eure Eingaben.",
                f"At {strom_ma} mA, the final volume is smaller than the initial volume. "
                "Please check your entries."
            ))

    messungen.append({
        "strom": strom_ma,
        "start": start,
        "ende": ende,
        "delta_3min": delta_drei_min,
        "delta_min": delta_pro_min,
        "k": konstante,
    })

konstanten = [m["k"] for m in messungen if m["k"] is not None]
mittelwert = sum(konstanten) / len(konstanten) if konstanten else None

SPALTEN = {
    "strom": lang("Strom I (mA)", "Current I (mA)"),
    "start": lang("Volumen H₂ Start (ml)", "Initial H₂ volume (ml)"),
    "ende": lang("Volumen H₂ Ende (ml)", "Final H₂ volume (ml)"),
    "delta_3min": lang("Delta H₂ (ml / 3 min)", "Change in H₂ (ml / 3 min)"),
    "delta_min": lang("Delta H₂ (ml / min)", "Change in H₂ (ml / min)"),
    "k": lang("Proportionalitätskonstante (ml / (min·A))",
              "Proportionality constant (ml / (min·A))"),
}

anzeige_zeilen = []
for m in messungen:
    anzeige_zeilen.append({
        SPALTEN["strom"]: str(m["strom"]),
        SPALTEN["start"]: formatiere_wert(m["start"], 1),
        SPALTEN["ende"]: formatiere_wert(m["ende"], 1),
        SPALTEN["delta_3min"]: formatiere_wert(m["delta_3min"], 2),
        SPALTEN["delta_min"]: formatiere_wert(m["delta_min"], 2),
        SPALTEN["k"]: formatiere_wert(m["k"], 2),
    })
anzeige_zeilen.append({
    SPALTEN["strom"]: lang("Mittelwert", "Mean"),
    SPALTEN["start"]: "–",
    SPALTEN["ende"]: "–",
    SPALTEN["delta_3min"]: "–",
    SPALTEN["delta_min"]: "–",
    SPALTEN["k"]: formatiere_wert(mittelwert, 2),
})
st.dataframe(pd.DataFrame(anzeige_zeilen), hide_index=True, use_container_width=True)

st.divider()
st.subheader(lang("Auswertung", "Evaluation"))
st.markdown(lang("**1. Volumenänderung über drei Minuten:**",
                 "**1. Volume change over three minutes:**"))
st.latex(r"\Delta V = V_{\mathrm{final}} - V_{\mathrm{initial}}")
st.markdown(lang("**2. Wasserstoffvolumen pro Minute:**", "**2. Hydrogen volume per minute:**"))
st.latex(r"\dot V = \frac{\Delta V}{3\,\mathrm{min}}")
st.markdown(lang("**3. Proportionalitätskonstante:**", "**3. Proportionality constant:**"))
st.latex(r"k = \frac{\dot V}{I\ (\mathrm{in\ A})}")
st.caption(lang(
    "Wichtig: 300 mA = 0,3 A; 400 mA = 0,4 A; 500 mA = 0,5 A.",
    "Important: 300 mA = 0.3 A; 400 mA = 0.4 A; 500 mA = 0.5 A."
))

if mittelwert is not None:
    st.metric(lang("Mittelwert der Proportionalitätskonstante",
                   "Mean proportionality constant"),
              f"{formatiere_wert(mittelwert)} ml/(min·A)")
    if len(konstanten) < len(STROMSTAERKEN_MA):
        st.caption(lang(
            f"Vorläufiger Mittelwert aus {len(konstanten)} von {len(STROMSTAERKEN_MA)} Messungen.",
            f"Provisional mean from {len(konstanten)} of {len(STROMSTAERKEN_MA)} measurements."
        ))
else:
    st.info(lang("Tragt Messwerte ein, um die Proportionalitätskonstante zu berechnen.",
                 "Enter measurements to calculate the proportionality constant."))

if st.button(lang("Ergebnisse anzeigen", "Show results"), type="primary", use_container_width=True):
    st.session_state["h2_v2_ergebnisse"] = True

if st.session_state.get("h2_v2_ergebnisse", False):
    st.subheader(lang("Vergleich eurer Messungen", "Comparison of your measurements"))
    gueltige_messungen = [m for m in messungen if m["k"] is not None]
    if not gueltige_messungen:
        st.info(lang("Für einen Vergleich benötigt ihr mindestens eine vollständige Messung.",
                     "At least one complete measurement is needed for comparison."))
    else:
        diagrammdaten = pd.DataFrame({
            lang("Strom I (mA)", "Current I (mA)"): [m["strom"] for m in gueltige_messungen],
            "k (ml/(min·A))": [m["k"] for m in gueltige_messungen],
        }).set_index(lang("Strom I (mA)", "Current I (mA)"))
        st.bar_chart(diagrammdaten,
                     x_label=lang("Stromstärke I (mA)", "Current I (mA)"),
                     y_label="k (ml/(min·A))")
        st.write(lang(
            "Vergleicht die berechneten Werte: Eine näherungsweise konstante "
            "Proportionalitätskonstante bedeutet, dass das erzeugte "
            "Wasserstoffvolumen pro Zeit näherungsweise proportional zur Stromstärke ist.",
            "Compare your calculated values: An approximately constant proportionality "
            "constant means that the hydrogen volume produced per unit of time is "
            "approximately proportional to the current."
        ))

st.divider()
st.subheader(lang("Fragen zur Auswertung", "Evaluation questions"))
st.write(lang(
    "1. Sind die berechneten Proportionalitätskonstanten für alle drei Stromstärken ähnlich groß?",
    "1. Are the calculated proportionality constants similar for all three current values?"
))
st.text_area(lang("Eure Antwort zu Frage 1", "Your answer to question 1"), key="h2_v2_antwort_1")
st.write(lang(
    "2. Welche Gründe könnten Unterschiede zwischen euren Messwerten erklären?",
    "2. What could explain differences between your measured values?"
))
st.text_area(lang("Eure Antwort zu Frage 2", "Your answer to question 2"), key="h2_v2_antwort_2")
st.write(lang(
    "3. Wie viel Wasserstoff würde euer Elektrolyseur bei 400 mA in 10 Minuten ungefähr erzeugen?",
    "3. Approximately how much hydrogen would your electrolyzer produce at 400 mA in 10 minutes?"
))
st.text_area(lang("Eure Antwort zu Frage 3", "Your answer to question 3"), key="h2_v2_antwort_3")
st.caption(lang(
    "Die drei Fragen sind als zusätzliche digitale Auswertung ergänzt; "
    "die Vorlage endet bei der Berechnung des Mittelwerts.",
    "These three questions are an additional digital evaluation; "
    "the original worksheet ends with the calculation of the mean."
))
