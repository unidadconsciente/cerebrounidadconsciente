import streamlit as st
import pandas as pd
import gspread

from google.oauth2.service_account import Credentials
def get_google_data():

    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key("1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4")

    avatar = pd.DataFrame(sheet.worksheet("Avatar_nuevo").get_all_records())
    contenido = pd.DataFrame(sheet.worksheet("Contenido").get_all_records())
    configuracion = pd.DataFrame(sheet.worksheet("Config_Archivos").get_all_records())
    opciones = pd.DataFrame(sheet.worksheet("Config_Opciones").get_all_records())

    avatar.columns = [c.strip() for c in avatar.columns]
    contenido.columns = [c.strip() for c in contenido.columns]
    configuracion.columns = [c.strip() for c in configuracion.columns]
    opciones.columns = [c.strip() for c in opciones.columns]

    return avatar, contenido, configuracion, opciones
