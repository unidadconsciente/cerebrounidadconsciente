def get_google_data():
    try:
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
        client = gspread.authorize(creds)
        
        # El error ocurre AQUÍ según tu Traceback
        sheet = client.open_by_key("1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4")
        
        avatar = pd.DataFrame(sheet.worksheet("Avatar_nuevo").get_all_records())
        contenido = pd.DataFrame(sheet.worksheet("Contenido").get_all_records())
        configuracion = pd.DataFrame(sheet.worksheet("Config_Archivos").get_all_records())
        
        # Usamos get_all_values para Config_Opciones por seguridad
        data_opciones = sheet.worksheet("Config_Opciones").get_all_values()
        opciones = pd.DataFrame(data_opciones[1:], columns=data_opciones[0])

        return avatar, contenido, configuracion, opciones

