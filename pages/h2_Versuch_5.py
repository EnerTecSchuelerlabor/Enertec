"""EnerTec – Wasserstoff Versuch 5 / Hydrogen Experiment 5: Efficiencies."""

import streamlit as st

from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang, get_language

st.set_page_config(page_title="EnerTec – Wasserstoff / Hydrogen – Experiment 5", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

BRENNWERT = 11.71  # J/ml H2 – value from the worksheet
VOLUMEN = 10.0  # ml H2


def zahl(wert, stellen=2):
    """Format numeric values according to the selected interface language."""
    ausgabe = f"{wert:.{stellen}f}"
    return ausgabe.replace(".", ",") if get_language() == "DE" else ausgabe


def ergebnis_pruefen(bezeichnung, eingabe, richtig, toleranz):
    """Compare the student's entered result with the computed model solution."""
    if eingabe is None:
        st.info(lang(
            f"{bezeichnung}: Noch keine eigene Lösung eingetragen.",
            f"{bezeichnung}: You haven't entered your own result yet.",
        ))
    elif abs(eingabe - richtig) <= toleranz:
        st.success(lang(f"{bezeichnung}: Richtig!", f"{bezeichnung}: Correct!"))
    else:
        st.warning(lang(
            f"{bezeichnung}: Überprüft eure Rechnung noch einmal.",
            f"{bezeichnung}: Please check your calculation again.",
        ))


st.title(lang("Versuch 5: Wirkungsgrade", "Experiment 5: Efficiencies"))
st.write(lang(
    "In diesem Versuch berechnet ihr die Wirkungsgrade des Elektrolyseurs, "
    "der Brennstoffzelle und des gesamten Systems. "
    "Tragt zunächst eure Ergebnisse selbst ein. Danach könnt ihr "
    "die berechneten Lösungen zum Vergleichen anzeigen lassen.",
    "In this experiment, you calculate the efficiencies of the electrolyzer, "
    "the fuel cell and the overall system. First enter your own results. "
    "Afterwards, you can display the calculated solutions and compare them with yours.",
))
st.divider()

st.subheader(lang("Information", "Information"))
st.write(lang(
    "Neben der bisher verwendeten elektrischen Energie gibt es weitere Energieformen. "
    "Dazu zählt die thermische Energie, die über den Elektrolyseur und die Brennstoffzelle "
    "während der elektrochemischen Reaktion abgegeben wird, sowie die chemische Energie, "
    "die im Wasserstoff gespeichert ist und bei seiner Umsetzung genutzt werden kann. "
    "Die Umwandlung ist nicht verlustfrei. Daher betrachten wir die Wirkungsgrade "
    "der einzelnen Komponenten und des Gesamtsystems.",
    "Besides the electrical energy considered so far, other forms of energy play a role. "
    "These include thermal energy released by the electrolyzer and fuel cell during "
    "the electrochemical reactions, and chemical energy stored in hydrogen that can be "
    "used when it reacts. Energy conversion is not loss-free. We therefore examine "
    "the efficiencies of the individual components and the entire system.",
))
st.divider()

st.subheader(lang("Aufgabe", "Task"))
st.write(lang(
    "Berechnet die **Teilwirkungsgrade des Elektrolyseurs und der Brennstoffzelle**, "
    "indem ihr die chemische Energie des Wasserstoffs mit der bereits berechneten "
    "elektrischen Energie aus Versuch 3 beziehungsweise Versuch 4 vergleicht. "
    "Berechnet zuerst den Brennwert für **10 ml Wasserstoff**. "
    "Tragt eure Ergebnisse in die Tabellen ein.",
    "Calculate the **individual efficiencies of the electrolyzer and fuel cell** "
    "by comparing the chemical energy of hydrogen with the electrical energy "
    "calculated in Experiment 3 and Experiment 4, respectively. "
    "First calculate the chemical energy associated with **10 ml of hydrogen**. "
    "Enter your results in the tables.",
))
st.info(lang(
    "**Vorgegebener Brennwert für Wasserstoff:** B = **11,71 J/ml**.\n\n"
    "**Wirkungsgrad:** η = nutzbare abgegebene Energie / zugeführte Energie. "
    "Für die Prozentangabe: η · 100 %.",
    "**Given energy value for hydrogen:** B = **11.71 J/ml**.\n\n"
    "**Efficiency:** η = useful output energy / input energy. "
    "For a percentage: η · 100%.",
))

st.divider()
st.subheader(lang("1. Chemische Energie von 10 ml H₂", "1. Chemical energy of 10 ml H₂"))
st.write(lang(
    "Berechnet zuerst die chemische Energie des Wasserstoffs.",
    "First calculate the chemical energy of the hydrogen.",
))
kopf = st.columns(3)
kopf[0].markdown(f"**{lang('Brennwert B (J/ml)', 'Energy value B (J/ml)')}**")
kopf[1].markdown(f"**{lang('Volumen H₂ (ml)', 'Volume H₂ (ml)')}**")
kopf[2].markdown(f"**{lang('Energie von 10 ml H₂ (J)', 'Energy of 10 ml H₂ (J)')}**")
zeile = st.columns(3)
zeile[0].write(zahl(BRENNWERT))
zeile[1].write(zahl(VOLUMEN, 0))
with zeile[2]:
    energie_chem_eigene = st.number_input(
        lang("Berechnete chemische Energie (J)", "Calculated chemical energy (J)"),
        min_value=0.0, value=None, step=0.1, format="%.2f",
        key="h2_v5_chem_eigene",
        placeholder=lang("Selbst berechnen", "Calculate it yourself"),
        label_visibility="collapsed",
    )

st.divider()
st.subheader(lang("2. Wirkungsgrad des Elektrolyseurs", "2. Electrolyzer efficiency"))
st.write(lang(
    "Übertragt die **zugeführte elektrische Energie** für 10 ml H₂ aus "
    "**Versuch 3**. Berechnet daraus den Wirkungsgrad des Elektrolyseurs.",
    "Enter the **electrical energy supplied** to produce 10 ml H₂ from "
    "**Experiment 3**. Use it to calculate the electrolyzer efficiency.",
))
energie_zu = st.number_input(
    lang("Zugeführte elektrische Energie aus Versuch 3 (J)",
         "Electrical input energy from Experiment 3 (J)"),
    min_value=0.0, value=None, step=1.0, format="%.2f",
    key="h2_v5_ein",
    placeholder=lang("Energie aus Versuch 3 eingeben", "Enter energy from Experiment 3"),
)
cols = st.columns(2)
with cols[0]:
    eta_el_abs = st.number_input(
        lang("Wirkungsgrad Elektrolyseur (absolut, z. B. 0,75)",
             "Electrolyzer efficiency (decimal, e.g. 0.75)"),
        min_value=0.0, value=None, step=0.01, format="%.4f",
        key="h2_v5_eta_el_abs",
    )
with cols[1]:
    eta_el_pro = st.number_input(
        lang("Wirkungsgrad Elektrolyseur (in %)", "Electrolyzer efficiency (in %)"),
        min_value=0.0, value=None, step=0.1, format="%.2f",
        key="h2_v5_eta_el_pro",
    )

st.divider()
st.subheader(lang("3. Wirkungsgrad der Brennstoffzelle", "3. Fuel cell efficiency"))
st.write(lang(
    "Übertragt die **abgegebene elektrische Energie** für 10 ml H₂ aus "
    "**Versuch 4**. Berechnet daraus den Wirkungsgrad der Brennstoffzelle.",
    "Enter the **electrical energy delivered** from 10 ml H₂ in "
    "**Experiment 4**. Use it to calculate the fuel cell efficiency.",
))
energie_ab = st.number_input(
    lang("Abgegebene elektrische Energie aus Versuch 4 (J)",
         "Electrical output energy from Experiment 4 (J)"),
    min_value=0.0, value=None, step=1.0, format="%.2f",
    key="h2_v5_aus",
    placeholder=lang("Energie aus Versuch 4 eingeben", "Enter energy from Experiment 4"),
)
cols = st.columns(2)
with cols[0]:
    eta_bz_abs = st.number_input(
        lang("Wirkungsgrad Brennstoffzelle (absolut, z. B. 0,35)",
             "Fuel cell efficiency (decimal, e.g. 0.35)"),
        min_value=0.0, value=None, step=0.01, format="%.4f",
        key="h2_v5_eta_bz_abs",
    )
with cols[1]:
    eta_bz_pro = st.number_input(
        lang("Wirkungsgrad Brennstoffzelle (in %)", "Fuel cell efficiency (in %)"),
        min_value=0.0, value=None, step=0.1, format="%.2f",
        key="h2_v5_eta_bz_pro",
    )

st.divider()
st.subheader(lang("4. Fragen", "4. Questions"))
st.write(lang(
    "**Welcher Wirkungsgrad ist höher: der des Elektrolyseurs oder der Brennstoffzelle?**",
    "**Which efficiency is higher: that of the electrolyzer or the fuel cell?**",
))
st.text_area(lang("Eure Antwort", "Your answer"), key="h2_v5_frage_1",
             placeholder=lang("Schreibt eure Überlegung auf ...", "Write down your reasoning ..."))
st.write(lang(
    "**Wie könntet ihr den Gesamtwirkungsgrad des Systems bestimmen?**",
    "**How could you determine the overall efficiency of the system?**",
))
st.text_area(lang("Eure Überlegung", "Your reasoning"), key="h2_v5_frage_2",
             placeholder=lang("Schreibt eure Überlegung auf ...", "Write down your reasoning ..."))

st.divider()
st.subheader(lang("5. Ergebnisse mit der Lösung vergleichen", "5. Compare your results with the solution"))
st.write(lang(
    "Wenn ihr eure Tabellen ausgefüllt habt, könnt ihr die Musterrechnung anzeigen. "
    "Für Versuch 3 wird **euer eigener Messwert** verwendet. "
    "Für Versuch 4 könnt ihr den Wert aus der Vorlage (**41,0 J**) eingeben.",
    "Once you have completed the tables, you can display the worked solution. "
    "For Experiment 3, **your own measurement** is used. "
    "For Experiment 4, you may enter the value from the worksheet (**41.0 J**).",
))

if "h2_v5_loesung_sichtbar" not in st.session_state:
    st.session_state["h2_v5_loesung_sichtbar"] = False

if st.button(
    lang("Musterlösung ausblenden", "Hide model solution")
    if st.session_state["h2_v5_loesung_sichtbar"]
    else lang("Musterlösung anzeigen und vergleichen", "Show model solution and compare"),
    type="primary", use_container_width=True,
):
    st.session_state["h2_v5_loesung_sichtbar"] = not st.session_state["h2_v5_loesung_sichtbar"]

if st.session_state["h2_v5_loesung_sichtbar"]:
    energie_chem = BRENNWERT * VOLUMEN
    st.markdown(lang("#### Tabelle 1: Chemische Energie", "#### Table 1: Chemical energy"))
    st.write(
        f"**B = {zahl(BRENNWERT)} J/ml**, "
        f"**V = {zahl(VOLUMEN, 0)} ml** → "
        f"**E₍chem₎ = B · V = {zahl(energie_chem)} J**"
    )
    ergebnis_pruefen(lang("Chemische Energie", "Chemical energy"),
                     energie_chem_eigene, energie_chem, 0.11)

    st.markdown(lang("#### Tabelle 2: Elektrolyseur", "#### Table 2: Electrolyzer"))
    if energie_zu is None or energie_zu <= 0:
        st.info(lang(
            "Tragt eine zugeführte Energie größer als 0 J aus Versuch 3 ein, "
            "um den Wirkungsgrad zu vergleichen.",
            "Enter an input energy greater than 0 J from Experiment 3 "
            "to compare the efficiency.",
        ))
    else:
        eta_el = energie_chem / energie_zu
        st.latex(r"\eta_{\mathrm{Elektrolyseur}}=\frac{E_{\mathrm{chemisch}}}{E_{\mathrm{zugefuehrt}}}")
        st.write(
            f"η = {zahl(energie_chem)} J / {zahl(energie_zu)} J "
            f"= **{zahl(eta_el, 4)}** = **{zahl(eta_el * 100)} %**"
        )
        ergebnis_pruefen(lang("Elektrolyseur (absolut)", "Electrolyzer (decimal)"),
                         eta_el_abs, eta_el, 0.005)
        ergebnis_pruefen(lang("Elektrolyseur (prozentual)", "Electrolyzer (percentage)"),
                         eta_el_pro, eta_el * 100, 0.11)
        if eta_el > 1:
            st.warning(lang(
                "Der berechnete Wirkungsgrad liegt über 100 %. "
                "Prüft die Messwerte und Einheiten aus Versuch 3.",
                "The calculated efficiency is above 100%. "
                "Check the measurements and units from Experiment 3.",
            ))

    st.markdown(lang("#### Tabelle 3: Brennstoffzelle", "#### Table 3: Fuel cell"))
    if energie_ab is None:
        st.info(lang(
            "Tragt die abgegebene Energie aus Versuch 4 ein, um den Wirkungsgrad zu vergleichen.",
            "Enter the output energy from Experiment 4 to compare the efficiency.",
        ))
    else:
        eta_bz = energie_ab / energie_chem
        st.latex(r"\eta_{\mathrm{Brennstoffzelle}}=\frac{E_{\mathrm{abgegeben}}}{E_{\mathrm{chemisch}}}")
        st.write(
            f"η = {zahl(energie_ab)} J / {zahl(energie_chem)} J "
            f"= **{zahl(eta_bz, 4)}** = **{zahl(eta_bz * 100)} %**"
        )
        ergebnis_pruefen(lang("Brennstoffzelle (absolut)", "Fuel cell (decimal)"),
                         eta_bz_abs, eta_bz, 0.005)
        ergebnis_pruefen(lang("Brennstoffzelle (prozentual)", "Fuel cell (percentage)"),
                         eta_bz_pro, eta_bz * 100, 0.11)
        if eta_bz > 1:
            st.warning(lang(
                "Der berechnete Wirkungsgrad liegt über 100 %. Prüft die Energie aus Versuch 4.",
                "The calculated efficiency is above 100%. Check the energy from Experiment 4.",
            ))

    st.markdown(lang("#### Fragen und Gesamtwirkungsgrad", "#### Questions and overall efficiency"))
    st.write(lang(
        "Der höhere Teilwirkungsgrad hängt von euren Messwerten ab. "
        "Den Gesamtwirkungsgrad ermittelt ihr durch Multiplikation "
        "der beiden Teilwirkungsgrade oder direkt aus dem Verhältnis "
        "von abgegebener zu zugeführter elektrischer Energie.",
        "Which component has the higher efficiency depends on your measured values. "
        "You can determine the overall efficiency by multiplying the two component "
        "efficiencies, or directly from the ratio of electrical output to input energy.",
    ))
    st.latex(
        r"\eta_{\mathrm{gesamt}}=\eta_{\mathrm{Elektrolyseur}}\cdot"
        r"\eta_{\mathrm{Brennstoffzelle}}="
        r"\frac{E_{\mathrm{abgegeben}}}{E_{\mathrm{zugefuehrt}}}"
    )
    if energie_zu is not None and energie_zu > 0 and energie_ab is not None:
        eta_gesamt = energie_ab / energie_zu
        st.success(lang("Gesamtwirkungsgrad:", "Overall efficiency:") +
                   f" **{zahl(eta_gesamt * 100)} %**")

st.divider()
st.caption(lang("EnerTec Workshop · Wasserstoff · Versuch 5",
                "EnerTec Workshop · Hydrogen · Experiment 5"))
