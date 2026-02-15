import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st

def get_google_data(sheet_id):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    doc = client.open_by_key(sheet_id)
    
    # Retornamos los DataFrames listos
    df_cont = pd.DataFrame(doc.worksheet("contenido").get_all_records())
    df_conf = pd.DataFrame(doc.worksheet("Config_Archivos").get_all_records())
    return df_cont, df_conf
