
import streamlit as st

from Solar import solar_main

st.set_page_config(
    page_title="EnerTec Workshop",
    layout="wide"
)

ENERTEC_LOGO = "img/enertec_logo.png"
STIFTUNG_LOGO = "img/enfo_logo.png"
LEHRSTUHL_LOGO = "img/aes_logo.png"

VERSUCH_1_BILD = "img/solar.png"
VERSUCH_2_BILD = "img/wind.png"
VERSUCH_3_BILD = "img/wasserstoff.png"

VERSUCH_1_SEITE = "Solar/solar_main.py" 
VERSUCH_2_SEITE = "Wind/wind_main.py"
VERSUCH_3_SEITE = "H2/h2_main.py"

APP_TITEL = "EnerTec Workshop"

EINLEITUNG = """
Herzlich Willkommen in der spannenden Welt der erneuerbaren Energien bei EnerTec an der Universität des Saarlandes!

Auf dieser Seite könnt ihr zwischen drei spannenden Experimenten wählen. Die Betreuer vor Ort unterstützen euch gerne bei der Auswahl und Durchführung. Klickt einfach auf eine Kachel, um direkt zur passenden Experimentierseite zu gelangen. Dort findet ihr Anleitungen, Zusatzinformationen und Hilfen zum Aufbau.

Bei Fragen meldet euch gerne bei den Betreuern. Ansonsten: Jetzt seid ihr dran! Viel Spaß beim Experimentieren!
"""

VERSUCH_1_TITEL = "Experiment mit Solarenergie"
VERSUCH_1_TEXT = (
    "Lernt mit Solarzellen vertraut zu machen und ihre Eigenschaften zu verstehen."
)

VERSUCH_2_TITEL = "Experiment mit Windenergie"
VERSUCH_2_TEXT = (
    "Lernt mit Windkraftanlagen vertraut zu werden und ihre Eigenschaften zu verstehen."
)

VERSUCH_3_TITEL = "Experiment mit Wasserstoffenergie"
VERSUCH_3_TEXT = (
    "Erforscht die Eigenschaften von Wasserstoff als Energieträger und seine Anwendung in der Energieversorgung."
)

HINWEIS_TEXT = (
    "Tipp: Auf den Versuchsseiten findet ihr zusätzliche Versuche und Erklärungen, "
    "Bilder zum Aufbau und Hilfen zur Durchführung."
)

IMPRESSUM_HTML = """
<div class="footer-box">
    <b>Impressum</b><br>
    EnerTec - Lehrstuhl für Automatisierungs- und Energiesysteme<br>
    Universität des Saarlandes<br>Campus<br>66123 Saarbrücken<br><br>
    <b>Website am Lehrstuhl</b><br>
    <a href="https://www.uni-saarland.de/lehrstuhl/frey/enertec.html" target="_blank">
    https://www.uni-saarland.de/lehrstuhl/frey/enertec.html
    </a><br><br>
    <b>Kontakt</b><br>
    <a href="mailto:enertec@uni-saarland.de">enertec@uni-saarland.de</a><br><br>
</div>
"""


st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    .hero-box {
        background: #f7f9fc;
        border-radius: 18px;
        padding: 1.6rem 2rem;
        margin-top: 0.4rem;
        margin-bottom: 2rem;
        border: 1px solid #e6ebf2;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.6rem;
        color: #1f2d3d;
    }

    .hero-text {
        font-size: 1.05rem;
        line-height: 1.7;
        color: #425466;
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-top: 0.2rem;
        margin-bottom: 1rem;
        color: #1f2d3d;
    }

    .card-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 0.8rem;
        margin-bottom: 0.4rem;
        color: #1f2d3d;
    }

    .card-text {
        font-size: 0.98rem;
        line-height: 1.55;
        color: #4f6378;
        min-height: 95px;
    }

    .small-note {
        color: #607080;
        font-size: 0.95rem;
        margin-top: 1rem;
    }

    .footer-box {
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #d9e1ea;
        color: #607080;
        font-size: 0.92rem;
        line-height: 1.7;
    }

    div[data-testid="stButton"] > button {
        border-radius: 12px;
        min-height: 48px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

def versuchskachel(bild, titel, text, button_text, zielseite, key):
    st.image(bild, use_container_width=True)
    st.markdown(f'<div class="card-title">{titel}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card-text">{text}</div>', unsafe_allow_html=True)
    if st.button(button_text, use_container_width=True, key=key):
        st.switch_page(zielseite)

left_col, center_col, right_col = st.columns([1.1, 2.6, 1.3], gap="large")

with left_col:
    st.image(ENERTEC_LOGO, use_container_width=True)

with center_col:
    st.markdown(f"""
    <div class="hero-box">
        <div class="hero-title">{APP_TITEL}</div>
        <div class="hero-text">{EINLEITUNG.replace(chr(10), "<br>")}</div>
    </div>
    """, unsafe_allow_html=True)

with right_col:
    st.image(STIFTUNG_LOGO, use_container_width=True)
    st.write("")
    st.image(LEHRSTUHL_LOGO, use_container_width=True)

st.markdown('<div class="section-title">Wählt ein Experiment</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    versuchskachel(
        bild=VERSUCH_1_BILD,
        titel=VERSUCH_1_TITEL,
        text=VERSUCH_1_TEXT,
        button_text="Zum Solarenergie-Experiment",
        zielseite=VERSUCH_1_SEITE,
        key="v1"
    )

with col2:
    versuchskachel(
        bild=VERSUCH_2_BILD,
        titel=VERSUCH_2_TITEL,
        text=VERSUCH_2_TEXT,
        button_text="Zum Windkraft-Experiment",
        zielseite=VERSUCH_2_SEITE,
        key="v2"
    )

with col3:
    versuchskachel(
        bild=VERSUCH_3_BILD,
        titel=VERSUCH_3_TITEL,
        text=VERSUCH_3_TEXT,
        button_text="Zum Wasserstoff-Experiment",
        zielseite=VERSUCH_3_SEITE,
        key="v3"
    )

st.markdown(
    f'<div class="small-note">{HINWEIS_TEXT}</div>',
    unsafe_allow_html=True
)

st.markdown(IMPRESSUM_HTML, unsafe_allow_html=True)
