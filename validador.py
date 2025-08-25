import pandas as pd
import streamlit as st

# --- Cargar datos ---
@st.cache_data
def load_data():
    # Asegúrate de que el archivo Excel esté en la misma carpeta que este script
    return pd.read_excel("control_bingo_1000_cartas_validador.xlsx", sheet_name="Ventas")

df = load_data()

# --- Interfaz ---
st.set_page_config(page_title="Validador de Bingo", page_icon="🎲", layout="centered")

st.title("🎲 Validador de Cartas de Bingo")
st.write("Escanea o pega el código QR de la carta para verificar si es válida.")

codigo = st.text_input("👉 Ingrese el código QR / ID (ejemplo: BINGO-CARTA-0001)")

if codigo:
    fila = df[df["Código QR / ID"].str.strip() == codigo.strip()]

    if fila.empty:
        st.error("❌ Código no encontrado en la base de datos")
    else:
        estado = fila["Estado de Pago"].values[0]
        jugador = fila["Nombre del Jugador"].values[0]
        email = fila["Email"].values[0]

        if estado == "Pagado":
            st.success(f"✅ Válido - Carta pagada")
            st.info(f"👤 Propietario: {jugador if jugador else 'No registrado'}\n📧 Email: {email if email else 'No disponible'}")
        else:
            st.warning("⚠️ Carta encontrada pero **NO pagada**")
