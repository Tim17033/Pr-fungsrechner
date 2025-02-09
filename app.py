import streamlit as st
import subprocess
import sys

# Seitenmenü erstellen
st.sidebar.title("📌 Hauptmenü")
option = st.sidebar.radio("Wähle einen Rechner:", [
    "🏠 Haushaltsrechner",
    "📊 Altersvorsorgerechner",
    "🏡 Baufinanzierungsrechner",
    "💰 Finanzierungsbedarfsrechner",
    "💳 Kreditrechner",
    "💸 Inflationsrechner",
    "🏡 Bausparrechner"
])

# Mapping der Auswahl auf Python-Dateien
rechner_mapping = {
    "🏠 Haushaltsrechner": "haushaltsrechner09.02.py",
    "📊 Altersvorsorgerechner": "altersvorsorgerechner09.02.py",
    "🏡 Baufinanzierungsrechner": "baufikreditrechner09.02.py",
    "💰 Finanzierungsbedarfsrechner": "finanzierungsbedarfbaufi09.02.py",
    "💳 Kreditrechner": "kreditrechner09.02.py",
    "💸 Inflationsrechner": "inflationsrechner09.02.py",
    "🏡 Bausparrechner": "bausparer09.02.py"
}

# Die entsprechende Datei ausführen
if option in rechner_mapping:
    script_path = rechner_mapping[option]
    st.write(f"Lade **{option}**...")
    exec(open(script_path).read(), globals())
