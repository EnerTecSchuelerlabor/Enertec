
"""Zweisprachige Seitennavigation für den EnerTec Workshop."""

import streamlit as st
from language import lang


def hide_default_sidebar_nav():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def solar_sidebar():
    with st.sidebar:
        st.title(lang("Solar-Experiment", "Solar Experiment"))

        if st.button(lang("← Zurück zur Startseite", "← Back to home"), use_container_width=True):
            st.switch_page("Startseite.py")

        st.divider()

        if st.button(lang("Solar Übersicht", "Solar Overview"), use_container_width=True):
            st.switch_page("pages/solar_main.py")

        if st.button(lang("Versuch 1", "Experiment 1"), use_container_width=True):
            st.switch_page("pages/s1_Versuch_1.py")

        if st.button(lang("Versuch 2", "Experiment 2"), use_container_width=True):
            st.switch_page("pages/s2_Versuch_2.py")

        if st.button(lang("Versuch 3", "Experiment 3"), use_container_width=True):
            st.switch_page("pages/s3_Versuch_3.py")

        if st.button(lang("Versuch 4", "Experiment 4"), use_container_width=True):
            st.switch_page("pages/s4_Versuch_4.py")

        if st.button(lang("Versuch 5", "Experiment 5"), use_container_width=True):
            st.switch_page("pages/s5_Versuch_5.py")

        if st.button(lang("Versuch 6", "Experiment 6"), use_container_width=True):
            st.switch_page("pages/s6_Versuch_6.py")

        st.divider()

        if st.button(lang("Aufbau Versuchskoffer", "Experiment Kit Setup"), use_container_width=True):
            st.switch_page("pages/s11_Aufbau_Versuchskoffer.py")

        if st.button(lang("Erklärung Solarenergie", "Solar Energy Explained"), use_container_width=True):
            st.switch_page("pages/s12_Erklärung_Solarenergie.py")

        if st.button(lang("Erklärung Reihenschaltung", "Series Circuits Explained"), use_container_width=True):
            st.switch_page("pages/s13_Erklärung_Reihenschaltung.py")

        if st.button(lang("Erklärung Parallelschaltung", "Parallel Circuits Explained"), use_container_width=True):
            st.switch_page("pages/s14_Erklärung_Parallelschaltung.py")

        if st.button(lang("Erklärung Wasser Modell", "Water Model Explained"), use_container_width=True):
            st.switch_page("pages/s15_Erklärung_Wasser_Modell.py")

        if st.button(lang("Erklärung Multimeter", "Multimeter Explained"), use_container_width=True):
            st.switch_page("pages/s16_Einstellung_Multimeter.py")

        if st.button(lang("Sammlung Videos", "Video Collection"), use_container_width=True):
            st.switch_page("pages/s17_Sammlung_Videos.py")


def wind_sidebar():
    with st.sidebar:
        st.title(lang("Wind-Experiment", "Wind Experiment"))

        if st.button(lang("← Zurück zur Startseite", "← Back to home"), use_container_width=True):
            st.switch_page("Startseite.py")

        st.divider()

        if st.button(lang("Wind Übersicht", "Wind Overview"), use_container_width=True):
            st.switch_page("pages/wind_main.py")

        if st.button(lang("Versuch 1", "Experiment 1"), use_container_width=True):
            st.switch_page("pages/w1_Versuch_1.py")

        if st.button(lang("Versuch 2", "Experiment 2"), use_container_width=True):
            st.switch_page("pages/w2_Versuch_2.py")

        if st.button(lang("Versuch 3", "Experiment 3"), use_container_width=True):
            st.switch_page("pages/w3_Versuch_3.py")

        if st.button(lang("Versuch 4", "Experiment 4"), use_container_width=True):
            st.switch_page("pages/w4_Versuch_4.py")

        st.divider()

        if st.button(lang("Aufbau Versuchskoffer", "Experiment Kit Setup"), use_container_width=True):
            st.switch_page("pages/w11_Aufbau_Versuchskoffer.py")

        if st.button(lang("Erklärung Windenergie", "Wind Energy Explained"), use_container_width=True):
            st.switch_page("pages/w12_Erklärung_Windenergie.py")

        if st.button(lang("Erklärung Wasser Modell", "Water Model Explained"), use_container_width=True):
            st.switch_page("pages/w15_Erklärung_Wasser_Modell.py")

        if st.button(lang("Erklärung Multimeter", "Multimeter Explained"), use_container_width=True):
            st.switch_page("pages/w16_Einstellung_Multimeter.py")

        if st.button(lang("Sammlung Videos", "Video Collection"), use_container_width=True):
            st.switch_page("pages/w17_Sammlung_Videos.py")


def h2_sidebar():
    with st.sidebar:
        st.title(lang("Wasserstoff-Experiment", "Hydrogen Experiment"))

        if st.button(lang("← Zurück zur Startseite", "← Back to home"), use_container_width=True):
            st.switch_page("Startseite.py")

        st.divider()

        if st.button(lang("Wasserstoff Übersicht", "Hydrogen Overview"), use_container_width=True):
            st.switch_page("pages/h2_main.py")

        if st.button(lang("Versuch 1", "Experiment 1"), use_container_width=True):
            st.switch_page("pages/h2_Versuch_1.py")

        if st.button(lang("Versuch 2", "Experiment 2"), use_container_width=True):
            st.switch_page("pages/h2_Versuch_2.py")

        if st.button(lang("Versuch 3", "Experiment 3"), use_container_width=True):
            st.switch_page("pages/h2_Versuch_3.py")

        if st.button(lang("Versuch 4", "Experiment 4"), use_container_width=True):
            st.switch_page("pages/h2_Versuch_4.py")

        if st.button(lang("Versuch 5", "Experiment 5"), use_container_width=True):
            st.switch_page("pages/h2_Versuch_5.py")

        st.divider()

        if st.button(lang("Aufbau Versuchskoffer", "Experiment Kit Setup"), use_container_width=True):
            st.switch_page("pages/h11_aufbau_versuchskoffer.py")

        if st.button(lang("Erklärung Wasserstoff", "Hydrogen Explained"), use_container_width=True):
            st.switch_page("pages/h12_Erklärung_Wasserstoff.py")

        if st.button(lang("Simulatoren & Rechner", "Simulators & Calculators"),use_container_width=True):
            st.switch_page("pages/h2_simulator.py")

        if st.button(lang("Erklärung Multimeter", "Multimeter Explained"), use_container_width=True):
            st.switch_page("pages/h16_Einstellung_multimeter.py")

        if st.button(lang("Sammlung Videos", "Video Collection"), use_container_width=True):
            st.switch_page("pages/h17_Sammlung_Videos.py")

        if st.button(lang("Wasserstoff Quiz", "Hydrogen Quiz"), use_container_width=True):
            st.switch_page("pages/h12_Quiz_Wasserstoff.py")

        st.divider()

        if st.button("Energy Challenge Game", use_container_width=True):
            st.switch_page("pages/energy_challenge.py")


