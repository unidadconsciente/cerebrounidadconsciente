import gspread
import pandas as pd
import streamlit as st
from google.oauth2.service_account import Credentials

# Agregamos caché para evitar el APIError por exceso de peticiones
@st.cache_data(ttl=600) 
def get_google_data():
    try:
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        # Cargamos credenciales desde st.secrets
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        # ID de la hoja de cálculo
        sheet_id = "1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4"
        sheet = client.open_by_key(sheet_id)
        
        # Carga de las 3 pestañas
        avatar = pd.DataFrame(sheet.worksheet("Avatar_nuevo").get_all_records())
        contenido = pd.DataFrame(sheet.worksheet("Contenido").get_all_records())
        configuracion = pd.DataFrame(sheet.worksheet("Config_Archivos").get_all_records())

        # Limpieza de nombres de columnas
        avatar.columns = [c.strip() for c in avatar.columns]
        contenido.columns = [c.strip() for c in contenido.columns]
        configuracion.columns = [c.strip() for c in configuracion.columns]

        return avatar, contenido, configuracion

    except Exception as e:
        st.error(f"Error al cargar datos: {e}")
        st.stop()
