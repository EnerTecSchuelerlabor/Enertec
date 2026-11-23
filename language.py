"""Gemeinsame Sprachsteuerung für alle Seiten des EnerTec-Workshops."""
import streamlit as st

DEFAULT_LANGUAGE = "DE"


def get_language():
    """Gibt die aktuell ausgewählte Sprache der Besuchersitzung zurück."""
    if "enertec_language" not in st.session_state:
        st.session_state["enertec_language"] = DEFAULT_LANGUAGE
    return st.session_state["enertec_language"]


def set_language(language):
    """Speichert die Auswahl für alle Seiten derselben Streamlit-Sitzung."""
    language = language.upper()
    if language not in ("DE", "EN"):
        raise ValueError("Sprache muss DE oder EN sein.")
    st.session_state["enertec_language"] = language


def lang(a: str, b: str) -> str:
    """Gibt a (Deutsch) oder b (Englisch) zurück."""
    return a if get_language() == "DE" else b
