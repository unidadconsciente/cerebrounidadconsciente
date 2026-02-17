import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st

def get_google_data():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key("1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4")
    
    # Carga y limpieza de nombres de columnas para evitar KeyErrors
    def get_df(name):
        df = pd.DataFrame(sheet.worksheet(name).get_all_records())
        df.columns = [str(c).strip() for c in df.columns] # Limpia espacios invisibles
        return df

    avatar = get_df("Avatar_nuevo")
    contenido = get_df("Contenido")
    configuracion = get_df("Config_Archivos")
    opciones = get_df("Config_Opciones")

    return avatar, contenido, configuracion, opciones
