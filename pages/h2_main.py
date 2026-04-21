import streamlit as st
from navigation import hide_default_sidebar_nav, h2_sidebar

st.set_page_config(page_title="Wind", layout="wide")

hide_default_sidebar_nav()
h2_sidebar()

st.logo('Logo_EnerTec_ohne_Hintergrund.png')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('Logo_Stiftung_ohne_Hintergrund.png', width=250)
    
with col2:
    st.image('Logo_EnerTec_ohne_Hintergrund.png', width=250)
    
with col3:
    st.image('Logo_AES_ohne_Hintergrund.png', width=250)
    
# ------------------------------------------------------------------------------------------------------------------------ #

st.title("Übersicht - Wasserstoffexperiment")

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Bitte lesen!')

st.write('Herzlich Willkommen im EnerTec!')

st.write('Ihr befindet euch auf der Startseite des Wasserstoff Workshops [TO DO].')

st.write('Diese Internetseite ist interaktiv aufgebaut. Ihr könnt in der Seitenleiste links die verschiedenen Seiten auswählen und entsprechend verwenden. Diese Webseite enthält mehrere Versuche aus denen ihr auswählen könnt, je nachdem was euch am meisten interessiert. Eine Übersicht über den Inhalt der Versuche findet ihr weiter unten.')

st.write('Zusätzlich gibt es noch weitere Seiten mit Zusatzinformationen und Erklärungen, wenn ihr euch intensiver mit einem Thema beschäftigen möchtet. Außerdem findet ihr auf der Seite "Aufbau Versuchskoffer" eine detaillierte Erklärung, wie ihr den Versuchskoffer für die Experimente aufbauen müsst. Auf jeder Seite eines Versuches findet ihr nochmals ein Bild zur Kontrolle des Aufbaus.')

st.write('Bei Fragen meldet euch gerne bei den Betreuern. Ansonsten: jetzt seid ihr dran, viel Spaß beim Experimentieren!')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.subheader('Übersicht Versuche')

st.write('Hier findet ihr eine Übersicht der angebotenen Versuche mit dem Titel und einer kurzen Beschreibung')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 1: x')

st.write('x.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 2: x')

st.write('x.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 3: x')

st.write('x.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #

st.write('Versuch 4: x')

st.write('x.')

st.write('---')

# ------------------------------------------------------------------------------------------------------------------------ #







