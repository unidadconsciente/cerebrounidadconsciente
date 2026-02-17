import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st

def get_google_data():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key("1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4")
    
    # Carga estándar para las que ya funcionan
    avatar = pd.DataFrame(sheet.worksheet("Avatar_nuevo").get_all_records())
    contenido = pd.DataFrame(sheet.worksheet("Contenido").get_all_records())
    configuracion = pd.DataFrame(sheet.worksheet("Config_Archivos").get_all_records())
    
    # CARGA EXPLÍCITA PARA CONFIG_OPCIONES (Para evitar el KeyError)
    # get_all_values trae la matriz cruda; convertimos la primera fila en columnas
    data_opciones = sheet.worksheet("Config_Opciones").get_all_values()
    opciones = pd.DataFrame(data_opciones[1:], columns=data_opciones[0])

    return avatar, contenido, configuracion, opciones
