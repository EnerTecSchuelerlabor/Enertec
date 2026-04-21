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
        st.title("Solar-Menü")

        if st.button("Solar Hauptseite", use_container_width=True):
            st.switch_page("pages/solar_main.py")

        if st.button("Aufbau Versuchskoffer", use_container_width=True):
            st.switch_page("pages/s11_Aufbau_Versuchskoffer.py")

        if st.button("Erklärung Solarenergie", use_container_width=True):
            st.switch_page("pages/s12_Erklärung_Solarenergie.py")

        if st.button("Erklärung Reihenschaltung", use_container_width=True):
            st.switch_page("pages/s13_Erklärung_Reihenschaltung.py")

        if st.button("Erklärung Parallelschaltung", use_container_width=True):
            st.switch_page("pages/s14_Erklärung_Parallelschaltung.py")

        if st.button("Versuch 1", use_container_width=True):
            st.switch_page("pages/s1_Versuch_1.py")

        if st.button("Versuch 2", use_container_width=True):
            st.switch_page("pages/s2_Versuch_2.py")

        if st.button("Versuch 3", use_container_width=True):
            st.switch_page("pages/s3_Versuch_3.py")

        st.divider()

        if st.button("Zur Startseite", use_container_width=True):
            st.switch_page("Startseite.py")
