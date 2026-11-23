import streamlit as st
from language import get_language, set_language, lang

st.set_page_config(page_title="EnerTec Workshop", page_icon="⚡", layout="wide")

# Vorhandene Dateinamen und Seitenpfade bleiben erhalten.
ENERTEC_LOGO = "img/enertec_logo.png"
STIFTUNG_LOGO = "img/enfo_logo.png"
LEHRSTUHL_LOGO = "img/aes_logo.png"

EXPERIMENTE = [
    {
        "bild": "img/solar.png",
        "name": ("Solarenergie", "Solar energy"),
        "titel": ("Experiment mit Solarenergie", "Solar energy experiment"),
        "text": (
            "Erfahrt, wie Solarzellen Licht in elektrische Energie umwandeln, und untersucht ihre Eigenschaften.",
            "Discover how solar cells convert sunlight into electricity and explore their properties.",
        ),
        "ziel": "pages/solar_main.py",
        "key": "solar",
        "nummer": "01",
    },
    {
        "bild": "img/wind.png",
        "name": ("Windenergie", "Wind energy"),
        "titel": ("Experiment mit Windenergie", "Wind energy experiment"),
        "text": (
            "Findet heraus, wie Windkraftanlagen funktionieren und welche Faktoren die Energieerzeugung beeinflussen.",
            "Find out how wind turbines work and what affects the amount of energy they produce.",
        ),
        "ziel": "pages/wind_main.py",
        "key": "wind",
        "nummer": "02",
    },
    {
        "bild": "img/wasserstoff.png",
        "name": ("Wasserstoff", "Hydrogen"),
        "titel": ("Experiment mit Wasserstoff", "Hydrogen experiment"),
        "text": (
            "Erforscht, wie Wasserstoff durch Elektrolyse entsteht und in einer Brennstoffzelle Strom liefert.",
            "Explore how electrolysis produces hydrogen and how a fuel cell generates electricity.",
        ),
        "ziel": "pages/h2_main.py",
        "key": "h2",
        "nummer": "03",
    },
]

st.markdown("""
<style>
  [data-testid="stSidebar"], [data-testid="collapsedControl"] {display:none;}
  .block-container {max-width: 1320px; padding-top: 1.15rem; padding-bottom: 2rem;}
  .enertec-eyebrow {font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;
    font-weight:750;color:#16858c;margin:.2rem 0 .5rem;}
  .enertec-heading {font-size:clamp(2rem,4vw,3.35rem);font-weight:820;
    letter-spacing:-.045em;line-height:1.12;margin:0 0 .85rem;}
  .enertec-lead {font-size:1.06rem;line-height:1.8;max-width:740px;
    color:var(--text-color);opacity:.84;}
  .enertec-strip {padding:.75rem 1rem;border-radius:12px;
    background:rgba(36,155,157,.09);border:1px solid rgba(36,155,157,.23);
    font-size:.94rem;line-height:1.6;}
  .enertec-num {font-size:.78rem;font-weight:800;letter-spacing:.1em;color:#188d93;}
  .enertec-card-title {font-size:1.25rem;font-weight:800;letter-spacing:-.015em;margin:.3rem 0 .4rem;}
  .enertec-card-copy {min-height:5.8rem;line-height:1.6;opacity:.85;font-size:.94rem;}
  .enertec-footer {border-top:1px solid rgba(125,135,145,.25);padding-top:1.2rem;
    margin-top:2rem;font-size:.9rem;line-height:1.85;opacity:.85;}
  .enertec-footer a {color:#159aa2;}
  div[data-testid="stButton"] > button {border-radius:12px;min-height:45px;font-weight:650;}
  div[data-testid="stVerticalBlockBorderWrapper"] {border-radius:18px;}
  @media(max-width:700px){.enertec-card-copy{min-height:auto}.block-container{padding-top:.7rem}}
</style>
""", unsafe_allow_html=True)

# Kopfzeile mit Logos und Sprache
logo_links, language_area = st.columns([4.3, 1.4], gap="large", vertical_alignment="center")
with logo_links:
    a, b, c = st.columns([1.2, 1, 1], gap="medium", vertical_alignment="center")
    with a:
        st.image(ENERTEC_LOGO, width=155)
    with b:
        st.image(STIFTUNG_LOGO, width=138)
    with c:
        st.image(LEHRSTUHL_LOGO, width=130)
with language_area:
    st.caption(lang("SPRACHE / LANGUAGE", "LANGUAGE / SPRACHE"))
    de_col, en_col = st.columns(2, gap="small")
    with de_col:
        st.button("🇩🇪 DE", key="choose_de", use_container_width=True,
                  type="primary" if get_language() == "DE" else "secondary",
                  on_click=set_language, args=("DE",))
    with en_col:
        st.button("🇬🇧 EN", key="choose_en", use_container_width=True,
                  type="primary" if get_language() == "EN" else "secondary",
                  on_click=set_language, args=("EN",))

st.write("")

with st.container(border=True):
    st.markdown('<div class="enertec-eyebrow">UNIVERSITÄT DES SAARLANDES · ENERTEC</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="enertec-heading">EnerTec Workshop ⚡</div>',
                unsafe_allow_html=True)
    st.markdown(
        f'<div class="enertec-lead">{lang("Willkommen in der Welt der erneuerbaren Energien! "
          "Entdeckt Solarenergie, Windkraft und Wasserstoff mit spannenden Experimenten. "
          "Wählt unten ein Thema aus und startet direkt mit dem Forschen.",
          "Welcome to the world of renewable energy! Explore solar power, wind energy "
          "and hydrogen through hands-on experiments. Choose a topic below and start exploring.")}</div>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        '<div class="enertec-strip">' + lang(
            "🧪 <b>So funktioniert’s:</b> Experiment auswählen → Anleitung ansehen → "
            "Aufbau mit den Betreuenden prüfen → ausprobieren und Messwerte eintragen.",
            "🧪 <b>How it works:</b> Choose an experiment → Read the instructions → "
            "Check your setup with a supervisor → Experiment and enter your measurements.")
        + '</div>', unsafe_allow_html=True,
    )

st.write("")
st.subheader(lang("Wählt euer Experiment", "Choose your experiment"))
st.caption(lang("Drei Themen – viele Möglichkeiten zum Entdecken.",
                "Three topics – plenty to explore."))

cols = st.columns(3, gap="large")
for col, exp in zip(cols, EXPERIMENTE):
    with col:
        with st.container(border=True):
            st.image(exp["bild"], use_container_width=True)
            st.markdown(f'<div class="enertec-num">EXPERIMENT {exp["nummer"]}</div>',
                        unsafe_allow_html=True)
            st.markdown(f'<div class="enertec-card-title">{lang(*exp["name"])}</div>',
                        unsafe_allow_html=True)
            st.markdown(f'<div class="enertec-card-copy">{lang(*exp["text"])}</div>',
                        unsafe_allow_html=True)
            if st.button(lang("Experiment starten", "Start experiment") + " →",
                         key="open_" + exp["key"], use_container_width=True,
                         type="primary" if exp["key"] == "h2" else "secondary"):
                st.switch_page(exp["ziel"])

st.write("")
st.info(lang(
    "💡 **Tipp:** Auf den Versuchsseiten findet ihr Aufbauhilfen, Erklärungen und Videos. "
    "Bei Fragen helfen euch die Betreuenden vor Ort.",
    "💡 **Tip:** Each experiment page includes setup instructions, explanations and videos. "
    "Ask the supervisors if you need any help."))

st.markdown('<div class="enertec-footer">', unsafe_allow_html=True)
foot_a, foot_b = st.columns([1.4, 1], gap="large")
with foot_a:
    st.markdown("**" + lang("Impressum", "Legal information") + "**")
    st.write("EnerTec – Lehrstuhl für Automatisierungs- und Energiesysteme  \n"
             "Universität des Saarlandes  \nCampus  \n66123 Saarbrücken")
with foot_b:
    st.markdown("**" + lang("Kontakt & weitere Informationen", "Contact & more information") + "**")
    st.markdown("[EnerTec – Universität des Saarlandes](https://www.uni-saarland.de/lehrstuhl/frey/enertec.html)")
    st.markdown("✉️ [enertec@uni-saarland.de](mailto:enertec@uni-saarland.de)")
st.markdown('</div>', unsafe_allow_html=True)
