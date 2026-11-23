from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang

st.set_page_config(page_title="EnerTec – Wasserstoff / Hydrogen – Experiment 1", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

# Die Abbildung liegt im Ordner img/ des Projekts.
AUFBAU_BILD = Path("img/h2_versuch1_aufbau.png")

st.title(lang("Versuch 1: Zersetzungsspannung und I-U-Kennlinie",
              "Experiment 1: Decomposition voltage and I-V characteristic"))
st.write(
    lang(
        "In diesem Versuch untersucht ihr, wie sich die Spannung am Elektrolyseur "
        "bei unterschiedlichen Stromstärken verändert. Aus euren Messwerten "
        "erstellt ihr die I-U-Kennlinie und bestimmt näherungsweise die Zersetzungsspannung.",
        "In this experiment you investigate how the voltage across the electrolyzer "
        "changes at different current values. Based on your measurements, "
        "you create the I-V characteristic and estimate the decomposition voltage."
    )
)
st.divider()

st.subheader(lang("Aufbau (gilt für alle Wasserstoff-Experimente)",
                  "Setup (applies to all hydrogen experiments)"))
if AUFBAU_BILD.exists():
    st.image(
        str(AUFBAU_BILD),
        caption=lang(
            "Versuchsaufbau mit Elektrolyseur, Messgeräten und Timer",
            "Experimental setup with electrolyzer, measuring instruments and timer"
        ),
        width=650
    )
else:
    st.info(
        lang(
            f"Aufbaubild ergänzen: {AUFBAU_BILD}",
            f"Please add the setup image: {AUFBAU_BILD}"
        )
    )

st.markdown(f"**{lang('Einstellung der Digitalmultimeter:', 'Digital multimeter settings:')}**")
st.write(lang("Spannungsmessung: **DC V**", "Voltage measurement: **DC V**"))
st.write(lang("Strommessung: **DC A**", "Current measurement: **DC A**"))
st.divider()

st.subheader(lang("Information", "Information"))
st.write(
    lang(
        "Ein Elektrolyseur verwendet elektrischen Strom, um eine chemische Reaktion "
        "herbeizuführen. Bei der Elektrolyse von Wasser wird Wasser in Wasserstoff "
        "und Sauerstoff zerlegt. Dabei entstehen die Gase im Volumenverhältnis 2:1.",
        "An electrolyzer uses electric current to drive a chemical reaction. "
        "During the electrolysis of water, water is split into hydrogen "
        "and oxygen. The gases are produced in a volume ratio of 2:1."
    )
)
st.latex(r"2\,H_2O \rightarrow 2\,H_2 + O_2")
st.write(
    lang(
        "Damit die Reaktion ablaufen kann, muss mindestens eine bestimmte elektrische "
        "Spannung anliegen. Diese wird als **Zersetzungsspannung** bezeichnet. "
        "In diesem Experiment bestimmt ihr sie näherungsweise mithilfe der I-U-Kennlinie "
        "des Elektrolyseurs.",
        "For this reaction to occur, at least a certain electrical voltage "
        "must be applied. This is called the **decomposition voltage**. "
        "In this experiment, you determine it approximately using the I-V characteristic "
        "of the electrolyzer."
    )
)
st.divider()

st.subheader(lang("Aufgabe", "Task"))
st.write(
    lang(
        "Beginnt mit **0 mA** und erhöht den Strom in Schritten von **50 mA** bis "
        "**500 mA**. Messt für jede Stromstärke die zugehörige Spannung und tragt "
        "sie unten in die digitale Tabelle ein. Anschließend könnt ihr eure Messwerte "
        "als I-U-Diagramm zeichnen lassen.",
        "Start at **0 mA** and increase the current in steps of **50 mA** up to "
        "**500 mA**. Measure the corresponding voltage for each current value and enter "
        "it into the digital table below. Afterwards, you can plot your measured values "
        "as an I-V diagram."
    )
)
st.info(
    lang(
        "**Hinweis zum ersten Messpunkt (0 mA):** Lest die Spannung erst ab, "
        "wenn sie sich stabilisiert hat und nicht mehr stark ansteigt.\n\n"
        "**Hinweis zu den weiteren Messpunkten:** Messt die Spannung nach jedem "
        "Umstellen möglichst nach der gleichen Zeit, zum Beispiel nach 10 Sekunden. "
        "Die Spannung kann sich mit der Zeit verändern.",
        "**Note for the first measurement point (0 mA):** Only read the voltage "
        "once it has stabilized and is no longer rising strongly.\n\n"
        "**Note for the following measurement points:** Measure the voltage after each "
        "adjustment after approximately the same amount of time, for example after 10 seconds. "
        "The voltage can change over time."
    )
)
st.divider()

st.subheader(lang("Digitale Messwerttabelle", "Digital measurement table"))
st.caption(
    lang(
        "Tragt die gemessene Spannung U in mV ein. Leere Felder werden nicht gezeichnet.",
        "Enter the measured voltage U in mV. Empty fields will not be plotted."
    )
)

stromwerte = list(range(0, 501, 50))
spannungen = []
spalten = st.columns(4)

for index, strom in enumerate(stromwerte):
    with spalten[index % 4]:
        spannung = st.number_input(
            lang(f"U bei I = {strom} mA (mV)", f"U at I = {strom} mA (mV)"),
            min_value=0.0,
            value=None,
            step=1.0,
            format="%.1f",
            key=f"h1_spannung_{strom}",
            placeholder=lang("Messwert eingeben", "Enter measurement value"),
        )
        spannungen.append(spannung)

tabelle = pd.DataFrame({
    lang("Strom I (mA)", "Current I (mA)"): stromwerte,
    lang("Spannung U (mV)", "Voltage U (mV)"): spannungen,
})
st.dataframe(tabelle.T, use_container_width=True)

if st.button(
    lang("I-U-Kennlinie zeichnen", "Plot I-V characteristic"),
    type="primary",
    use_container_width=True
):
    st.session_state["h1_diagramm_anzeigen"] = True

if st.session_state.get("h1_diagramm_anzeigen", False):
    messpunkte = [
        (strom, spannung)
        for strom, spannung in zip(stromwerte, spannungen)
        if spannung is not None
    ]

    if not messpunkte:
        st.warning(
            lang(
                "Bitte gebt zuerst mindestens einen Spannungswert ein.",
                "Please enter at least one voltage value first."
            )
        )
    else:
        st.subheader(lang("I-U-Kennlinie des Elektrolyseurs",
                          "I-V characteristic of the electrolyzer"))

        x = np.array([punkt[0] for punkt in messpunkte], dtype=float)
        y = np.array([punkt[1] for punkt in messpunkte], dtype=float)

        st.write(
            lang(
                "Für die Abschätzung der Zersetzungsspannung könnt ihr den annähernd "
                "geradlinigen Abschnitt der Kennlinie auswählen. Die Gerade wird bis "
                "zur Spannungsachse bei **I = 0 mA** verlängert.",
                "To estimate the decomposition voltage, you can select the approximately "
                "linear part of the characteristic curve. The fitted line is then extended "
                "to the voltage axis at **I = 0 mA**."
            )
        )

        grenze = st.select_slider(
            lang("Geradenabschnitt ab Stromstärke (mA)",
                 "Linear section starting from current value (mA)"),
            options=list(range(0, 501, 50)),
            value=200,
            key="h1_fitschwelle",
        )

        fit_maske = x >= grenze
        fit_moeglich = np.count_nonzero(fit_maske) >= 2

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.plot(
            x, y, "o-", linewidth=1.8,
            label=lang("Eure Messwerte", "Your measured values")
        )

        if fit_moeglich:
            steigung, achsenabschnitt = np.polyfit(x[fit_maske], y[fit_maske], 1)
            fit_x = np.linspace(0, max(x), 200)
            ax.plot(
                fit_x,
                steigung * fit_x + achsenabschnitt,
                "--",
                label=lang("Verlängerte Ausgleichsgerade", "Extended best-fit line")
            )
            ax.scatter(
                [0], [achsenabschnitt],
                zorder=5,
                label=lang("Geschätzte Zersetzungsspannung", "Estimated decomposition voltage")
            )

        ax.set_title(lang("I-U-Kennlinie Elektrolyseur", "Electrolyzer I-V characteristic"))
        ax.set_xlabel(lang("Strom I in mA", "Current I in mA"))
        ax.set_ylabel(lang("Spannung U in mV", "Voltage U in mV"))
        ax.set_xlim(0, 500)
        ax.set_xticks(stromwerte)
        ax.grid(alpha=0.3)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

        if fit_moeglich:
            st.metric(
                lang("Geschätzte Zersetzungsspannung", "Estimated decomposition voltage"),
                f"{achsenabschnitt:.1f} mV"
            )
            st.caption(
                lang(
                    "Dieser Wert ist eine mathematische Näherung aus den gewählten Messpunkten, "
                    "nicht automatisch ein exakter physikalischer Wert. Wählt nur den "
                    "tatsächlich annähernd linearen Teil eurer Kennlinie.",
                    "This value is a mathematical approximation based on the selected measurement points, "
                    "not automatically an exact physical value. Only use the section of your curve "
                    "that is actually approximately linear."
                )
            )
        else:
            st.info(
                lang(
                    "Für die Ausgleichsgerade werden mindestens zwei Messwerte im gewählten Bereich benötigt.",
                    "At least two measured values in the selected range are required for the best-fit line."
                )
            )

        st.divider()
        st.subheader(lang("Fragen", "Questions"))
        st.write(
            lang(
                "Nähert den annähernd linearen Verlauf eurer Kennlinie durch eine Gerade an. "
                "Welchen Schnittpunkt mit der Spannungsachse erhaltet ihr? "
                "Dieser Wert ist eure näherungsweise Zersetzungsspannung.",
                "Approximate the nearly linear part of your characteristic curve with a straight line. "
                "What intercept do you obtain with the voltage axis? "
                "This value is your approximate decomposition voltage."
            )
        )

        st.text_area(
            lang("Wie groß ist eure Zersetzungsspannung?",
                 "What is your decomposition voltage?"),
            key="h1_antwort_1"
        )
        st.text_area(
            lang("Was fällt euch am Verlauf eurer Kurve auf?",
                 "What do you notice about the shape of your curve?"),
            key="h1_antwort_2"
        )

        with st.expander(lang("Erklärung zur Auswertung", "Explanation of the evaluation")):
            st.write(
                lang(
                    "Im annähernd linearen Bereich steigt die Spannung mit wachsender "
                    "Stromstärke ungefähr geradlinig an. Verlängert man diesen Abschnitt "
                    "bis I = 0 mA, erhält man den Achsenabschnitt als experimentelle "
                    "Näherung der Zersetzungsspannung.",
                    "In the approximately linear region, the voltage increases almost linearly "
                    "with increasing current. If you extend this section back to I = 0 mA, "
                    "the intercept gives an experimental approximation of the decomposition voltage."
                )
            )
