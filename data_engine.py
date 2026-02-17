import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st

def get_google_data():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    
    # Acceso directo al ID verificado
    sheet = client.open_by_key("1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4")
    
    # Carga de las 4 pestañas necesarias
    avatar = pd.DataFrame(sheet.worksheet("Avatar_nuevo").get_all_records())
    contenido = pd.DataFrame(sheet.worksheet("Contenido").get_all_records())
    configuracion = pd.DataFrame(sheet.worksheet("Config_Archivos").get_all_records())
    opciones = pd.DataFrame(sheet.worksheet("Config_Opciones").get_all_records())

    return avatar, contenido, configuracion, opciones
