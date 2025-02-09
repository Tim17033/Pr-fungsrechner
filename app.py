import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Finanzrechner", page_icon="💰", layout="wide")

# Custom CSS for modern button grid
st.markdown(
    """
    <style>
    .button-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        justify-content: center;
    }
    .button-grid button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 30px;
        text-align: center;
        font-size: 18px;
        margin: 10px;
        border-radius: 10px;
        cursor: pointer;
        transition: 0.3s;
    }
    .button-grid button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.title("💰 Finanzrechner Übersicht")
st.markdown("Wähle einen Rechner aus, um loszulegen:")

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

# Moderne Button-Grid
selected_option = None
st.markdown('<div class="button-grid">', unsafe_allow_html=True)
for label in rechner_mapping.keys():
    if st.button(label):
        selected_option = label
st.markdown('</div>', unsafe_allow_html=True)

# Die entsprechende Datei ausführen
if selected_option:
    script_path = rechner_mapping[selected_option]
    st.write(f"Lade **{selected_option}**...")
    exec(open(script_path).read(), globals())

