"""EnerTec – zweisprachige Multimeter-Hilfe für die Wasserstoffversuche."""

import streamlit as st
from navigation import hide_default_sidebar_nav, h2_sidebar
from language import lang

st.set_page_config(page_title="EnerTec Wasserstoff – Multimeter", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

st.logo('Solar/Logo_EnerTec_ohne_Hintergrund.png')

col1, col2, col3 = st.columns(3)
with col1:
    st.image('Solar/Logo_Stiftung_ohne_Hintergrund.png', width=250)
with col2:
    st.image('Solar/Logo_EnerTec_ohne_Hintergrund.png', width=250)
with col3:
    st.image('Solar/Logo_AES_ohne_Hintergrund.png', width=250)

st.title(lang('Einstellung Multimeter – Wasserstoff', 'Multimeter settings – Hydrogen'))

st.write(lang(
    'Bei den Wasserstoffexperimenten messt ihr die elektrische Spannung und die '
    'Stromstärke am Elektrolyseur beziehungsweise an der Brennstoffzelle. '
    'Da die Einstellung der Multimeter immer wieder zu Problemen führen kann, '
    'findet ihr hier die Einstellmöglichkeiten für die beiden Gerätetypen '
    '„Schwarz“ und „Rot“. Die Bilder sind dieselben wie im Solar-Workshop.',
    'In the hydrogen experiments, you measure voltage and current at the '
    'electrolyzer or the fuel cell. Since setting up the multimeters can sometimes '
    'be confusing, this page explains the settings for the two meter types, '
    '“Black” and “Red”. The pictures are the same as in the solar workshop.'
))

st.subheader(lang('Worauf müsst ihr achten?', 'What should you pay attention to?'))
st.markdown(lang(
    '''
1. **Richtiges Multimeter wählen:** Verwendet die Anleitung für euer schwarzes oder rotes Gerät.
2. **Messbuchsen prüfen:** Das schwarze Kabel gehört in **COM**. Das rote Kabel kommt in die passende Buchse für Spannung beziehungsweise Stromstärke.
3. **Richtige Polung beachten:** Achtet beim Anschließen auf Plus und Minus. Ist die Polung vertauscht, kann ein negatives Vorzeichen angezeigt werden.
4. **Messart und Messbereich einstellen:** Für die Wasserstoffversuche benötigt ihr **Gleichspannung (DC V)** und **Gleichstrom (DC A)**. Wählt einen geeigneten Messbereich und überschreitet die zulässigen Werte des Geräts nicht.
''',
    '''
1. **Choose the correct multimeter:** Follow the instructions for your black or red meter.
2. **Check the sockets:** The black lead goes into **COM**. The red lead goes into the appropriate voltage or current socket.
3. **Check polarity:** Pay attention to positive and negative connections. Reversed polarity may produce a negative reading.
4. **Select the measurement type and range:** The hydrogen experiments require **DC voltage (DC V)** and **DC current (DC A)**. Choose a suitable range and do not exceed the meter's ratings.
'''
))

st.warning(lang(
    '**Wichtig:** Spannung wird **parallel** zum zu untersuchenden Bauteil gemessen, '
    'Stromstärke **in Reihe**. Schließt ein auf Strommessung eingestelltes Multimeter '
    'niemals direkt parallel an eine Spannungsquelle an – dadurch kann ein Kurzschluss entstehen. '
    'Steckt Kabel nur bei ausgeschaltetem beziehungsweise stromlosem Aufbau um und fragt bei Unsicherheit die Betreuer.',
    '**Important:** Voltage is measured **in parallel** with the component being tested; '
    'current is measured **in series**. Never connect a multimeter set to current measurement '
    'directly across a voltage source – this can cause a short circuit. '
    'Only move leads when the setup is switched off or de-energized, and ask a supervisor if unsure.'
))

st.divider()
st.subheader(lang(
    'Welche Einstellungen benötigt ihr im Wasserstoff-Workshop?',
    'Which settings do you need for the hydrogen workshop?'
))

versuche = [
    (
        '**Versuch 1 – I-U-Kennlinie:** Ihr messt die Spannung am Elektrolyseur und die '
        'Stromstärke im Stromkreis. Die Stromwerte reichen laut Versuchsanleitung von '
        '0 bis 500 mA. Achtet darauf, dass der eingestellte Messbereich diesen Wert abdeckt.',
        '**Experiment 1 – I-V characteristic:** Measure the voltage across the electrolyzer '
        'and the current in the circuit. According to the instructions, current ranges from '
        '0 to 500 mA. Make sure the selected measurement range covers these values.'
    ),
    (
        '**Versuch 2 – Proportionalitätskonstante:** Die Stromstärke wird auf 300, '
        '400 beziehungsweise 500 mA eingestellt. Prüft die Anzeige und die Einheit am Multimeter.',
        '**Experiment 2 – Proportionality constant:** Set the current to 300, '
        '400 or 500 mA. Check the displayed value and unit on the multimeter.'
    ),
    (
        '**Versuch 3 – Zugeführte Energie:** Die Stromstärke beträgt 400 mA. '
        'Für die Energieberechnung messt ihr zusätzlich die Spannung in Volt.',
        '**Experiment 3 – Electrical energy supplied:** The current is 400 mA. '
        'You also measure the voltage in volts to calculate the energy.'
    ),
    (
        '**Versuch 4 – Abgegebene Energie:** An der Brennstoffzelle betrachtet ihr '
        'Spannung und Stromstärke; die Musterwerte in der Anleitung sind in Volt und Ampere angegeben.',
        '**Experiment 4 – Electrical energy delivered:** Examine voltage and current at '
        'the fuel cell; the reference values in the instructions are given in volts and amperes.'
    ),
    (
        '**Versuch 5 – Wirkungsgrade:** Ihr verwendet die zuvor ermittelten '
        'Energiewerte. Achtet besonders auf die Umrechnung von mA in A und mV in V.',
        '**Experiment 5 – Efficiencies:** Use the energy values determined in the previous '
        'experiments. Pay particular attention to converting mA to A and mV to V.'
    ),
]
for de, en in versuche:
    st.write(lang(de, en))

with st.expander(lang('Einheiten kurz erklärt', 'Units explained briefly')):
    st.markdown(lang(
        '''
- **1000 mA = 1 A** → zum Beispiel **400 mA = 0,400 A**.
- **1000 mV = 1 V** → zum Beispiel **1600 mV = 1,6 V**.
- Für die Formel **E = U · I · t** setzt ihr **U in V**, **I in A** und **t in s** ein. Das Ergebnis ist die Energie **E in Joule (J)**.
''',
        '''
- **1000 mA = 1 A** → for example, **400 mA = 0.400 A**.
- **1000 mV = 1 V** → for example, **1600 mV = 1.6 V**.
- For **E = U · I · t**, use **U in V**, **I in A**, and **t in s**. The result is energy **E in joules (J)**.
'''
    ))

st.info(lang(
    'Die passenden Buchsen und Drehreglerstellungen unterscheiden sich je nach '
    'Multimeter. Orientiert euch an den folgenden Bildern und lasst die Einstellung '
    'im Zweifel von einem Betreuer kontrollieren.',
    'The correct sockets and rotary-switch positions depend on the multimeter. '
    'Follow the pictures below and ask a supervisor to check your settings if in doubt.'
))

st.divider()
st.subheader(lang('Multimeter Schwarz', 'Black multimeter'))

schwarz = [
    (
        'Schwarz 2000mV', 'Black 2000mV', 'Solar/schwarz_2000mV.png',
        'Gleichspannung im Millivoltbereich. Nur verwenden, wenn der erwartete Messwert innerhalb dieses Bereichs liegt.',
        'DC voltage in the millivolt range. Use only if the expected reading is within this range.'
    ),
    (
        'Schwarz 20V', 'Black 20V', 'Solar/schwarz_20V.png',
        'Gleichspannung in Volt. Für Spannungen oberhalb von 2000 mV ist dieser Bereich häufig geeigneter.',
        'DC voltage in volts. This range is often more suitable for voltages above 2000 mV.'
    ),
    (
        'Schwarz 2000mA', 'Black 2000mA', 'Solar/schwarz_2000mA.png',
        'Gleichstrom im Milliamperebereich. Bei 300–500 mA muss die entsprechende Buchse laut Gerätebeschriftung geeignet sein.',
        'DC current in milliamperes. For 300–500 mA, confirm that the socket is rated for this current according to the meter label.'
    ),
    (
        'Schwarz 10A', 'Black 10A', 'Solar/schwarz_10A.png',
        'Gleichstrom im Amperebereich. Beachtet dafür die passende 10-A-Buchse und die Gerätegrenzen.',
        'DC current in amperes. Use the matching 10 A socket and observe the meter ratings.'
    ),
]

for titel_de, titel_en, bild, hinweis_de, hinweis_en in schwarz:
    st.markdown(f'#### {lang(titel_de, titel_en)}')
    st.image(bild, width=500)
    st.caption(lang(hinweis_de, hinweis_en))
    st.divider()

st.subheader(lang('Multimeter Rot', 'Red multimeter'))

rot = [
    (
        'Rot mV', 'Red mV', 'Solar/rot_mV.png',
        'Gleichspannung im Millivoltbereich; prüft, ob der Messwert im zulässigen Bereich liegt.',
        'DC voltage in the millivolt range; check that the reading is within the permitted range.'
    ),
    (
        'Rot V', 'Red V', 'Solar/rot_V.png',
        'Gleichspannung in Volt; für die Spannung des Elektrolyseurs beziehungsweise der Brennstoffzelle.',
        'DC voltage in volts; for measuring the voltage of the electrolyzer or fuel cell.'
    ),
    (
        'Rot mA', 'Red mA', 'Solar/rot_mA.png',
        'Gleichstrom im Milliamperebereich. Wichtig: Dieser Eingang kann je nach Gerät geringer abgesichert sein als 500 mA. Vor dem Messen Gerätebeschriftung prüfen!',
        'DC current in milliamperes. Important: Depending on the meter, this input may be rated below 500 mA. Check the meter label before measuring!'
    ),
    (
        'Rot A', 'Red A', 'Solar/rot_A.png',
        'Gleichstrom im Amperebereich; verwendet die dazugehörige Strombuchse und achtet auf die maximal zulässige Stromstärke.',
        'DC current in amperes; use the appropriate current socket and observe the maximum permitted current.'
    ),
]

for titel_de, titel_en, bild, hinweis_de, hinweis_en in rot:
    st.markdown(f'#### {lang(titel_de, titel_en)}')
    st.image(bild, width=500)
    st.caption(lang(hinweis_de, hinweis_en))
    st.divider()

st.subheader(lang('Häufige Fehler', 'Common mistakes'))
st.markdown(lang(
    '''
- **Anzeige bleibt bei 0:** Prüft zunächst den Stromkreis, die Verbindungskabel und die eingestellte Messart.
- **Anzeige zeigt „OL“ oder „1“:** Der Messbereich könnte überschritten sein. Messung unterbrechen und einen geeigneten Bereich wählen.
- **Negatives Vorzeichen:** Prüft, ob Plus und Minus vertauscht sind.
- **Unplausible Stromwerte:** Prüft, ob die richtige Strombuchse und der passende Messbereich eingestellt sind. Eine durchgebrannte Gerätesicherung kann ebenfalls die Ursache sein.
''',
    '''
- **Display remains at 0:** Check the circuit, connecting leads and selected measurement mode first.
- **Display shows “OL” or “1”:** The selected range may be exceeded. Stop measuring and select a suitable range.
- **Negative sign:** Check whether positive and negative connections are reversed.
- **Implausible current readings:** Check that the correct current socket and range are selected. A blown meter fuse may also be the cause.
'''
))

st.warning(lang(
    'Falls etwas nicht funktioniert: Nicht durch Ausprobieren beliebig umstecken. Fragt die Betreuer vor Ort.',
    'If something does not work, do not randomly reconnect leads to troubleshoot. Ask the supervisors on site.'
))
