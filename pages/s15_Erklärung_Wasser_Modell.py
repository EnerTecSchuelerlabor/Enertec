# Header #

import streamlit as st
import matplotlib.pyplot as plt

import streamlit as st
from navigation import hide_default_sidebar_nav, solar_sidebar

st.set_page_config(page_title="Solar", layout="wide")

hide_default_sidebar_nav()
solar_sidebar()

st.set_page_config(page_title = "EnerTec Solar Workshop", layout = "wide")

st.logo('Solar/Logo_EnerTec_ohne_Hintergrund.png')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('Solar/Logo_Stiftung_ohne_Hintergrund.png', width=250)
    
with col2:
    st.image('Solar/Logo_EnerTec_ohne_Hintergrund.png', width=250)
    
with col3:
    st.image('Solar/Logo_AES_ohne_Hintergrund.png', width=250)
    
# ------------------------------------------------------------------------------------------------------------------------ #

st.title('Erklärung Wasser Modell')

st.write('Auf dieser Seite wird das Wasser Modell erklärt welches große Ähnlichkeiten zum elektrischen Strom aufweist und so erlaubt die verschiedenen Größen miteinander zu vergleichen.')

st.write('---')

st.write('Mit dem Wasser Modell lassen sich die drei grundlegenden Größen des Stromkreises erklären: die Stromstärke, die elektrische Spannung und der Widerstand.')

st.write('Dabei entspricht die elektrische Spannung dem Höhenunterschied des Wassers, also einer Druckdifferenz. Die Spannung bzw. deren Höhe gibt an, wie stark Elektronen durch den Stromkreis "gedrückt" werden. Entsprechend verhält sich eine Spannungsquelle (wie z.B. eine Solarzelle) wie eine Pumpe, die Elektronen auf ein höheres Niveau befördert und ihnen so eine gewisse Energie verleiht.')

st.write('Ähnlich dazu entspricht die Stromstärke dem Volumen bzw. der Menge des Wassers das fließt. Wenn ihr in einem der Experimente seht, dass die Stromstärke steigt, bedeutet das, dass mehr Elektronen durch den Stromkreis fließen.')

st.write('Die letzte wichtige Größe stellt der Widerstand dar, der wie der Name schon vermuten lässt, einen Widerstand für das Wasser bzw. die Elektronen darstellt. In unserem Fall sprechen wir häufig von einem elektrischen Verbraucher, wie z.B. einer Glühbirne oder einem Motor, da solch ein Widerstand dem Wasser bzw. dem Strom ein wenig an Kraft nimmt und ein Hindernis darstellt.')

st.image('Solar/page_15_pic_1.png')

st.write('Quelle: https://www.elektrotechnik-einfach.de/spannung/')

st.write('---')

st.write('Das Bild unten beschreibt den Zusammenhang zwischen dem elektrischen Strom und Wasser nochmals anschaulich. Dabei sieht man hier, wie eine Pumpe und ein Wasserrad jeweils eine Spannungsquelle bzw. einen Widerstand (hier eine Glühbirne) darstellen. Die Wasserbecken an sich können als eine Art Energiespeicher z.B. eine Batterie angesehen werden.')

st.image('Solar/page_15_pic_2.png')

st.write('Quelle: https://physikkommunizieren.de/themenfelder/7_strom/d_modelle/')

st.write('---')

