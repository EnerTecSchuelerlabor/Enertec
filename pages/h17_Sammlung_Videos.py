"""EnerTec DE/EN-Videosammlung für Wasserstoff."""

import streamlit as st
from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang, get_language

st.set_page_config(page_title="EnerTec – Wasserstoff-Videos", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

st.title(lang("Sammlung Videos – Wasserstoff", "Video collection – Hydrogen"))
st.write(lang(
    "Hier findet ihr drei ausgewählte YouTube-Videos zu Wasserstoff, Elektrolyse "
    "und Brennstoffzellen. Die Videos wechseln zusammen mit eurer Sprachauswahl.",
    "Here are three selected YouTube videos about hydrogen, electrolysis "
    "and fuel cells. The videos change according to your selected language.",
))

# Die bisherigen drei deutschen Videos bleiben unverändert.
VIDEOS_DE = [
    {
        "url": "https://www.youtube.com/watch?v=XR3VMV3tXsE",
        "titel": "1 – Grüner Wasserstoff: Herstellung und Einsatz",
        "beschreibung": "Was ist grüner Wasserstoff, wie entsteht er und wo kann er genutzt werden?",
        "quelle": "youknow",
        "bezug": "Hintergrundwissen für alle fünf Wasserstoffversuche.",
    },
    {
        "url": "https://www.youtube.com/watch?v=EzBAGN2Jx7Y",
        "titel": "2 – Elektrolyse: Was passiert dabei?",
        "beschreibung": "Das Prinzip der Elektrolyse und die chemischen Vorgänge dahinter.",
        "quelle": "Chemie – simpleclub",
        "bezug": "Besonders passend zu Versuch 1 und Versuch 3.",
    },
    {
        "url": "https://www.youtube.com/watch?v=bcTxQw87o4Y",
        "titel": "3 – Brennstoffzelle: Aus Wasserstoff wird Strom",
        "beschreibung": "Anschauliche Erklärung des Zusammenspiels von Elektrolyse, Wasserstoff und Brennstoffzelle.",
        "quelle": "Christian Korbinian",
        "bezug": "Besonders passend zu Versuch 4 und Versuch 5.",
    },
]

# Drei englischsprachige YouTube-Videos.
VIDEOS_EN = [
    {
        "url": "https://www.youtube.com/watch?v=MC5JkmwcjF0",
        "titel": "1 – Hydrogen: The fuel of the future",
        "beschreibung": "How green hydrogen is produced and why it can help store renewable energy.",
        "quelle": "Max Planck Institute for Sustainable Materials",
        "bezug": "Background for all five hydrogen experiments.",
    },
    {
        "url": "https://www.youtube.com/watch?v=GAfhuUqknPU",
        "titel": "2 – Water electrolysis explained in 60 seconds",
        "beschreibung": "A short explanation of how electricity splits water into hydrogen and oxygen.",
        "quelle": "DVGW",
        "bezug": "Especially useful for experiments 1, 2 and 3.",
    },
    {
        "url": "https://www.youtube.com/watch?v=zzuq2VETdtc",
        "titel": "3 – How does a hydrogen fuel cell work?",
        "beschreibung": "How a fuel cell converts hydrogen and oxygen into electrical energy.",
        "quelle": "RICE Cymru / University of South Wales",
        "bezug": "Especially useful for experiments 4 and 5.",
    },
]

videos = VIDEOS_DE if get_language() == "DE" else VIDEOS_EN

st.caption(lang(
    "Aktuelle Videoauswahl: 🇩🇪 Deutsch",
    "Current video selection: 🇬🇧 English",
))

for index, video in enumerate(videos):
    st.divider()
    st.subheader(video["titel"])
    col_video, col_info = st.columns([1.7, 1], gap="large")
    with col_video:
        st.video(video["url"])
    with col_info:
        st.write(video["beschreibung"])
        st.info(video["bezug"])
        st.caption(lang("Kanal / Quelle: ", "Channel / source: ") + video["quelle"])
        st.link_button(
            lang("Auf YouTube öffnen", "Open on YouTube"),
            video["url"],
        )

st.divider()
st.info(lang(
    "Die Videos ergänzen die Versuchsanleitungen. Für den Aufbau gelten "
    "die Hinweise des EnerTec-Versuchskoffers und die Anweisungen der Betreuung.",
    "These videos supplement the experiment instructions. For the setup, "
    "follow the EnerTec equipment instructions and your supervisor's guidance.",
))
