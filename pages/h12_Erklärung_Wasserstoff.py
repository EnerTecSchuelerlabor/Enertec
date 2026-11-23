"""EnerTec – Wasserstoff verstehen: Chemie, Physik und Anwendungen (DE/EN).

Die Diagramme werden mit Matplotlib erzeugt: Es sind keine zusätzlichen
Bilddateien nötig. Die Sprachauswahl kommt aus language.py.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import streamlit as st

from language import lang
from navigation import hide_default_sidebar_nav, h2_sidebar

st.set_page_config(page_title="EnerTec – Wasserstoff / Hydrogen", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

# =============================================================================
# Universelle Diagramme: nur Formeln / chemische Symbole; daher in DE und EN gleich
# =============================================================================

def flow_diagram():
    """Chemischer Kreislauf: Elektrolyse und Brennstoffzelle (schematisch)."""
    fig, ax = plt.subplots(figsize=(11.5, 4.1))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.4)
    ax.axis("off")

    def node(x, y, w, h, text, color):
        box = FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.12,rounding_size=0.2",
            facecolor=color, edgecolor="#26415b", linewidth=1.2,
        )
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=13, fontweight="bold", color="#17324d")

    def arrow(start, end, color="#426b8c"):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=17,
            linewidth=2.2, color=color, connectionstyle="arc3,rad=0",
        ))

    node(0.25, 1.65, 2.0, 1.1, r"$H_2O$", "#d9efff")
    node(3.05, 1.65, 2.4, 1.1, r"$2H_2O\;\rightarrow\;2H_2+O_2$", "#e5f5fc")
    node(6.28, 1.65, 2.05, 1.1, r"$2H_2+O_2$", "#e6f5e6")
    node(9.1, 1.65, 2.5, 1.1, r"$2H_2+O_2\;\rightarrow\;2H_2O$", "#fff0d7")
    arrow((2.35, 2.2), (2.96, 2.2))
    arrow((5.55, 2.2), (6.18, 2.2))
    arrow((8.43, 2.2), (9.0, 2.2))

    # Energien sind Ein- und Ausgänge, keine zusätzliche Stoffreaktion.
    ax.text(4.25, 3.67, r"$E_{\mathrm{el}}\;\downarrow$", fontsize=16,
            ha="center", va="center", color="#a34f18", fontweight="bold")
    arrow((4.25, 3.42), (4.25, 2.9), "#c77b34")
    arrow((10.3, 1.53), (10.3, 0.98), "#c77b34")
    ax.text(10.3, 0.56, r"$E_{\mathrm{el}}+Q$", fontsize=15,
            ha="center", color="#a34f18", fontweight="bold")
    ax.text(0.25, 0.48, "H₂O  →  H₂  →  H₂O", fontsize=12,
            color="#47647d", va="center")
    fig.tight_layout(pad=0.4)
    return fig


def gas_ratio_diagram():
    """Stoffmengen- und Volumenverhältnis bei gleicher T und gleichem p."""
    fig, ax = plt.subplots(figsize=(7.4, 3.3))
    fig.patch.set_facecolor("white")
    bars = ax.bar([r"$H_2$", r"$O_2$"], [2, 1], width=0.55,
                  color=["#2f84b9", "#72b47e"])
    for bar, value in zip(bars, [2, 1]):
        ax.text(bar.get_x() + bar.get_width()/2, value + 0.06, str(value),
                ha="center", va="bottom", fontsize=15, fontweight="bold")
    ax.set_ylim(0, 2.45)
    ax.set_yticks([])
    ax.spines[["left", "right", "top"]].set_visible(False)
    ax.spines["bottom"].set_color("#bdcbd6")
    ax.tick_params(axis="x", length=0, labelsize=14)
    fig.tight_layout()
    return fig


st.title(lang("Wasserstoff verstehen", "Understanding hydrogen"))
st.write(lang(
    "Hier erfahrt ihr, was bei der Elektrolyse und in der Brennstoffzelle "
    "chemisch und physikalisch passiert – und wofür Wasserstoff genutzt werden kann.",
    "Discover the chemistry and physics behind electrolysis and fuel cells "
    "and find out what hydrogen can be used for."
))

st.info(lang(
    "**Merksatz:** Wasserstoff ist ein **Energieträger**, keine ursprüngliche Energiequelle. "
    "Um ihn aus Wasser herzustellen, muss zunächst Energie zugeführt werden.",
    "**Key point:** Hydrogen is an **energy carrier**, not a primary energy source. "
    "Energy must first be supplied to produce it from water."
))

st.subheader(lang("Der Kreislauf auf einen Blick", "The cycle at a glance"))
fig = flow_diagram()
st.pyplot(fig, use_container_width=True)
plt.close(fig)
st.caption(lang(
    "Vereinfachtes Schema: Links wird Wasser mit elektrischer Energie zerlegt. "
    "Rechts wird die chemische Energie der Gase in einer Brennstoffzelle teilweise "
    "als elektrische Energie nutzbar; außerdem entsteht Wärme (Q).",
    "Simplified diagram: On the left, electrical energy splits water. "
    "On the right, a fuel cell converts some of the gases' chemical energy "
    "into useful electrical energy; heat (Q) is also released."
))

chemie, physik, anwendung = st.tabs([
    lang("Chemie", "Chemistry"),
    lang("Physik und Messungen", "Physics and measurements"),
    lang("Anwendungen", "Applications"),
])

with chemie:
    st.subheader(lang("1. Elektrolyse: Wasser wird zerlegt", "1. Electrolysis: splitting water"))
    st.write(lang(
        "Der **Elektrolyseur** bekommt elektrischen Strom vom Regulator. "
        "Durch elektrochemische Reaktionen wird Wasser in **Wasserstoff (H₂)** "
        "und **Sauerstoff (O₂)** zerlegt. Die beiden Gase werden im Versuchskoffer "
        "getrennt gesammelt.",
        "The **electrolyzer** receives electrical power from the regulator. "
        "Electrochemical reactions split water into **hydrogen (H₂)** and "
        "**oxygen (O₂)**. The two gases are collected separately in the kit."
    ))
    st.latex(r"2\,H_2O\;\xrightarrow{\text{elektrische Energie}}\;2\,H_2+O_2" if lang("DE", "EN") == "DE"
             else r"2\,H_2O\;\xrightarrow{\text{electrical energy}}\;2\,H_2+O_2")
    st.write(lang(
        "Ein Wassermolekül enthält zwei Wasserstoffatome und ein Sauerstoffatom. "
        "Für die Bildung der Gase müssen chemische Bindungen verändert werden. "
        "Dafür braucht die Elektrolyse Energie.",
        "A water molecule contains two hydrogen atoms and one oxygen atom. "
        "Producing the gases requires chemical bonds to be rearranged, "
        "which needs an input of energy."
    ))

    left, right = st.columns([1.3, 1], gap="large")
    with left:
        st.markdown(lang("**Warum entsteht mehr Wasserstoff?**", "**Why is more hydrogen produced?**"))
        st.write(lang(
            "Aus zwei Wassermolekülen entstehen zwei H₂-Moleküle und ein O₂-Molekül. "
            "Bei gleicher Temperatur und gleichem Druck entspricht das ungefähr "
            "dem **Gasvolumenverhältnis H₂ : O₂ = 2 : 1**. Das könnt ihr an den "
            "Messzylindern des Gasspeichers beobachten.",
            "Two water molecules yield two H₂ molecules and one O₂ molecule. "
            "At equal temperature and pressure, this gives an approximate "
            "**gas-volume ratio H₂ : O₂ = 2 : 1**. You can observe it in the "
            "gas storage measuring cylinders."
        ))
    with right:
        fig = gas_ratio_diagram()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
        st.caption(lang("Theoretisches Volumenverhältnis", "Theoretical volume ratio"))

    st.divider()
    st.subheader(lang("2. Brennstoffzelle: Aus Gasen wird Strom", "2. Fuel cell: generating electricity"))
    st.write(lang(
        "In der **Brennstoffzelle** reagieren Wasserstoff und Sauerstoff "
        "elektrochemisch miteinander. Dabei entsteht wieder Wasser. "
        "Die Reaktion ist so aufgebaut, dass Elektronen durch einen äußeren "
        "Stromkreis fließen können. Diesen Strom könnt ihr mit dem Multimeter "
        "messen oder mit einer geeigneten Last nutzen.",
        "Inside the **fuel cell**, hydrogen and oxygen react electrochemically "
        "to form water again. The reaction is arranged so electrons can flow "
        "through an external circuit. You can measure this current with a "
        "multimeter or use it to power a suitable load."
    ))
    st.latex(r"2\,H_2+O_2\;\longrightarrow\;2\,H_2O+\text{Energie}" if lang("DE", "EN") == "DE"
             else r"2\,H_2+O_2\;\longrightarrow\;2\,H_2O+\text{energy}")
    st.warning(lang(
        "**Wichtig:** Die Brennstoffzelle verbrennt den Wasserstoff nicht in einer "
        "offenen Flamme. Die Reaktion läuft kontrolliert an Elektroden ab. "
        "Wasserstoff ist trotzdem leicht entzündlich – arbeitet nur unter Aufsicht.",
        "**Important:** A fuel cell does not burn hydrogen in an open flame. "
        "The reaction proceeds in a controlled way at electrodes. "
        "Hydrogen is still highly flammable – work only under supervision."
    ))

with physik:
    st.subheader(lang("Spannung, Strom und Energie", "Voltage, current and energy"))
    st.write(lang(
        "**Spannung U (Volt)** beschreibt den elektrischen Antrieb für Ladungen. "
        "**Stromstärke I (Ampere)** gibt an, wie viel elektrische Ladung pro "
        "Sekunde fließt. Mit einem Multimeter messt ihr Spannung **parallel** "
        "und Strom **in Reihe** zum betreffenden Stromkreis.",
        "**Voltage U (volts)** describes the electrical potential difference driving charge. "
        "**Current I (amperes)** is the amount of electric charge flowing per second. "
        "Use a multimeter **in parallel** to measure voltage and **in series** "
        "to measure current."
    ))
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(lang("**Elektrische Leistung**", "**Electrical power**"))
        st.latex(r"P=U\cdot I")
        st.caption(lang("P in Watt (W)", "P in watts (W)"))
    with col2:
        st.markdown(lang("**Elektrische Energie**", "**Electrical energy**"))
        st.latex(r"E=P\cdot t=U\cdot I\cdot t")
        st.caption(lang("E in Joule (J), t in Sekunden (s)", "E in joules (J), t in seconds (s)"))
    st.write(lang(
        "Für Rechnungen gilt: **1.000 mA = 1 A** und **1.000 mV = 1 V**. "
        "Wenn Spannung oder Strom während des Versuchs schwanken, wird die "
        "Energie mit geeigneten Mittelwerten näherungsweise bestimmt.",
        "For calculations: **1,000 mA = 1 A** and **1,000 mV = 1 V**. "
        "If voltage or current changes during an experiment, energy can be "
        "estimated using suitable average values."
    ))
    st.divider()
    st.subheader(lang("Warum geht Energie verloren?", "Why is some energy lost?"))
    st.write(lang(
        "Bei Elektrolyse und Brennstoffzelle entstehen unter anderem Wärmeverluste "
        "und elektrische Verluste. Daher kommt bei der Rückumwandlung in Strom "
        "**weniger elektrische Energie heraus, als zuvor zum Herstellen des "
        "Wasserstoffs hineingesteckt wurde**. Der Wirkungsgrad beschreibt, "
        "welcher Anteil der eingesetzten Energie als gewünschte Nutzenergie ankommt.",
        "Electrolysis and fuel cells involve losses, including heat and electrical "
        "losses. This means **less electrical energy is recovered than was "
        "originally used to produce the hydrogen**. Efficiency describes "
        "how much of the input energy becomes useful output energy."
    ))
    st.latex(r"\eta=\frac{E_{\mathrm{nutz}}}{E_{\mathrm{zugefuehrt}}}\cdot100\%")
    st.caption(lang(
        "In Versuch 3–5 messt und berechnet ihr die Energie und die Wirkungsgrade selbst.",
        "In experiments 3–5, you measure and calculate energy and efficiency yourselves."
    ))
    with st.expander(lang("Zusatz: Die I-U-Kennlinie", "Extra: The I–V curve")):
        st.write(lang(
            "Beim Elektrolyseur steigt der Strom erst deutlich an, wenn eine "
            "ausreichende Spannung anliegt. Die gemessene Kennlinie hängt unter "
            "anderem von den Elektroden, der Temperatur und den Verlusten ab. "
            "In Versuch 1 bestimmt ihr daraus näherungsweise die Zersetzungsspannung.",
            "In an electrolyzer, current increases noticeably only once a "
            "sufficient voltage is applied. The measured curve depends on "
            "electrodes, temperature and losses, among other factors. In "
            "experiment 1, you estimate the decomposition voltage from this curve."
        ))

with anwendung:
    st.subheader(lang("Was kann man mit Wasserstoff machen?", "What can hydrogen be used for?"))
    uses = [
        ("🏭", "Industrie", "Industry",
         "Wasserstoff wird als Rohstoff verwendet, etwa für Ammoniak. Er kann auch "
         "bei Prozessen helfen, die bisher fossile Rohstoffe benötigen.",
         "Hydrogen is used as a feedstock, for example to make ammonia. "
         "It can also help replace fossil materials in some processes."),
        ("🚚", "Verkehr", "Transport",
         "Brennstoffzellen können Fahrzeuge elektrisch antreiben, besonders dort, "
         "wo Batterien allein schwierig einzusetzen sind.",
         "Fuel cells can power electric vehicles, especially where using "
         "batteries alone is difficult."),
        ("🔋", "Energiespeicherung", "Energy storage",
         "Mit erneuerbarem Strom kann Wasserstoff hergestellt, gespeichert und "
         "bei Bedarf wieder genutzt werden – allerdings mit Energieverlusten.",
         "Renewable electricity can produce hydrogen that is stored and used "
         "later – although conversion causes energy losses."),
        ("⚙️", "Strom und Wärme", "Power and heat",
         "Brennstoffzellen können elektrische Energie und nutzbare Wärme liefern, "
         "beispielsweise für bestimmte stationäre Anwendungen.",
         "Fuel cells can supply electricity and useful heat, for example "
         "in certain stationary systems."),
    ]
    for symbol, de_title, en_title, de_text, en_text in uses:
        st.markdown(f"### {symbol} {lang(de_title, en_title)}")
        st.write(lang(de_text, en_text))
    st.info(lang(
        "**Grüner Wasserstoff** wird durch Elektrolyse mit erneuerbarem Strom "
        "hergestellt. Wie klimafreundlich Wasserstoff ist, hängt besonders "
        "davon ab, wie er erzeugt und transportiert wird.",
        "**Green hydrogen** is produced by electrolysis using renewable "
        "electricity. Its climate impact depends strongly on how it is "
        "produced and transported."
    ))

st.divider()
st.subheader(lang("Bezug zu euren Experimenten", "How this relates to your experiments"))
experiments = [
    (1, "Zersetzungsspannung und I-U-Kennlinie", "Decomposition voltage and I–V curve"),
    (2, "Wasserstoffmenge und Stromstärke", "Hydrogen volume and current"),
    (3, "Energiezufuhr zum Elektrolyseur", "Energy input to the electrolyzer"),
    (4, "Energieabgabe der Brennstoffzelle", "Energy output of the fuel cell"),
    (5, "Wirkungsgrade vergleichen", "Comparing efficiencies"),
]
for number, de, en in experiments:
    st.write(f"**{lang('Versuch', 'Experiment')} {number}:** {lang(de, en)}")

with st.expander(lang("Wissenscheck: Drei kurze Fragen", "Knowledge check: three quick questions")):
    questions = [
        (
            "Was stellt der Elektrolyseur her?", "What does the electrolyzer produce?",
            ["Strom", "Wasserstoff und Sauerstoff", "Nur Wärme"],
            ["Electricity", "Hydrogen and oxygen", "Heat only"], 1,
        ),
        (
            "Wofür ist der Timer in Versuch 3 wichtig?",
            "Why do you need the timer in experiment 3?",
            ["Zur Messung der Zeit", "Zur Spannungsmessung", "Zur Gasspeicherung"],
            ["To measure time", "To measure voltage", "To store gas"], 0,
        ),
        (
            "Warum ist der elektrische Gesamtwirkungsgrad kleiner als 100 %?",
            "Why is the overall electrical efficiency below 100%?",
            ["Wegen Energieverlusten", "Weil Wasser fehlt", "Weil H₂ kein Gas ist"],
            ["Because of energy losses", "Because water is missing", "Because H₂ is not a gas"], 0,
        ),
    ]
    for i, (q_de, q_en, options_de, options_en, correct) in enumerate(questions):
        # Gespeicherte Indexantworten sind unabhängig von der Sprachauswahl.
        current = st.session_state.get(f"h2_knowledge_{i}")
        labels = [lang(d, e) for d, e in zip(options_de, options_en)]
        choice = st.radio(lang(q_de, q_en), options=range(3),
                          format_func=lambda n, labels=labels: labels[n],
                          key=f"h2_knowledge_{i}", index=None)
        if choice is not None:
            if choice == correct:
                st.success(lang("Richtig!", "Correct!"))
            else:
                st.info(lang("Überlegt noch einmal.", "Try again."))

st.caption(lang(
    "EnerTec – Grundlagen für die Wasserstoffexperimente. "
    "Die Grafiken sind schematisch und nicht maßstabsgetreu.",
    "EnerTec – background for the hydrogen experiments. "
    "The diagrams are schematic and not drawn to scale."
))
