import gspread
import pandas as pd
import streamlit as st
from google.oauth2.service_account import Credentials

def get_google_data():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key("1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4")
    
    # Solo cargamos las 3 pestañas esenciales
    avatar = pd.DataFrame(sheet.worksheet("Avatar_nuevo").get_all_records())
    contenido = pd.DataFrame(sheet.worksheet("Contenido").get_all_records())
    configuracion = pd.DataFrame(sheet.worksheet("Config_Archivos").get_all_records())

    # Limpieza de columnas
    for df in [avatar, contenido, configuracion]:
        df.columns = [str(c).strip() for c in df.columns]

    return avatar, contenido, configuracion
