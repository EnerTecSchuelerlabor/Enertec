import streamlit as st

def hide_default_sidebar_nav():
    st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

def solar_sidebar():
    with st.sidebar:
        st.title("Solar-Experiment")

        if st.button("← Zurück zur Startseite", use_container_width=True):
            st.switch_page("Startseite.py")

        st.divider()

        if st.button("Solar Übersicht", use_container_width=True):
            st.switch_page("pages/solar_main.py")

        if st.button("Versuch 1", use_container_width=True):
            st.switch_page("pages/s1_Versuch_1.py")

        if st.button("Versuch 2", use_container_width=True):
            st.switch_page("pages/s2_Versuch_2.py")

        if st.button("Versuch 3", use_container_width=True):
            st.switch_page("pages/s3_Versuch_3.py")

        if st.button("Versuch 4", use_container_width=True):
            st.switch_page("pages/s4_Versuch_4.py")

        if st.button("Versuch 5", use_container_width=True):
            st.switch_page("pages/s5_Versuch_5.py")

        if st.button("Versuch 6", use_container_width=True):
            st.switch_page("pages/s6_Versuch_6.py")

        st.divider()

        if st.button("Aufbau Versuchskoffer", use_container_width=True):
            st.switch_page("pages/s11_Aufbau_Versuchskoffer.py")

        if st.button("Erklärung Solarenergie", use_container_width=True):
            st.switch_page("pages/s12_Erklärung_Solarenergie.py")

        if st.button("Erklärung Reihenschaltung", use_container_width=True):
            st.switch_page("pages/s13_Erklärung_Reihenschaltung.py")

        if st.button("Erklärung Parallelschaltung", use_container_width=True):
            st.switch_page("pages/s14_Erklärung_Parallelschaltung.py")

        if st.button("Erklärung Wasser Modell", use_container_width=True):
            st.switch_page("pages/s15_Erklärung_Wasser_Modell.py")

        if st.button("Erklärung Multimeter", use_container_width=True):
            st.switch_page("pages/s16_Einstellung_Multimeter.py")

        if st.button("Sammlung Videos", use_container_width=True):
            st.switch_page("pages/s17_Sammlung_Videos.py")



def wind_sidebar():
    with st.sidebar:
        st.title("Wind-Experiment")

        if st.button("← Zurück zur Startseite", use_container_width=True):
            st.switch_page("Startseite.py")

        st.divider()

        if st.button("Wind Übersicht", use_container_width=True):
            st.switch_page("pages/wind_main.py")

        if st.button("Versuch 1", use_container_width=True):
            st.switch_page("pages/w1_Versuch_1.py")

        if st.button("Versuch 2", use_container_width=True):
            st.switch_page("pages/w2_Versuch_2.py")

        if st.button("Versuch 3", use_container_width=True):
            st.switch_page("pages/w3_Versuch_3.py")

        if st.button("Versuch 4", use_container_width=True):
            st.switch_page("pages/w4_Versuch_4.py")

        st.divider()

        if st.button("Aufbau Versuchskoffer", use_container_width=True):
            st.switch_page("pages/w11_Aufbau_Versuchskoffer.py")

        if st.button("Erklärung Windenergie", use_container_width=True):
            st.switch_page("pages/w12_Erklärung_Windenergie.py")

        if st.button("Erklärung Wasser Modell", use_container_width=True):
            st.switch_page("pages/w15_Erklärung_Wasser_Modell.py")

        if st.button("Erklärung Multimeter", use_container_width=True):
            st.switch_page("pages/w16_Einstellung_Multimeter.py")

        if st.button("Sammlung Videos", use_container_width=True):
            st.switch_page("pages/w17_Sammlung_Videos.py")


def h2_sidebar():
    with st.sidebar:
        st.title("Wasserstoff-Experiment [TO DO]")

        if st.button("← Zurück zur Startseite", use_container_width=True):
            st.switch_page("Startseite.py")

        st.divider()

        if st.button("Wasserstoff Übersicht", use_container_width=True):
            st.switch_page("pages/h2_main.py")

        if st.button("Versuch 1", use_container_width=True):
            st.switch_page("pages/h1_Versuch_1.py")

        if st.button("Versuch 2", use_container_width=True):
            st.switch_page("pages/h2_Versuch_2.py")

        if st.button("Versuch 3", use_container_width=True):
            st.switch_page("pages/h3_Versuch_3.py")

        if st.button("Versuch 4", use_container_width=True):
            st.switch_page("pages/h4_Versuch_4.py")

        st.divider()

        if st.button("Aufbau Versuchskoffer", use_container_width=True):
            st.switch_page("pages/h11_Aufbau_Versuchskoffer.py")

        if st.button("Erklärung Wasserstoff", use_container_width=True):
            st.switch_page("pages/h12_Erklärung_Windenergie.py")

        if st.button("Erklärung Wasser Modell", use_container_width=True):
            st.switch_page("pages/h15_Erklärung_Wasser_Modell.py")

        if st.button("Erklärung Multimeter", use_container_width=True):
            st.switch_page("pages/h16_Einstellung_Multimeter.py")

        if st.button("Sammlung Videos", use_container_width=True):
            st.switch_page("pages/h17_Sammlung_Videos.py")

