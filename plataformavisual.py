import streamlit as st
# AQUÍ VINCULAMOS LOS MÓDULOS
from data_engine import get_google_data
from prompt_engine import build_master_prompt

# Ahora puedes usar las funciones como si estuvieran aquí
df_cont, df_conf = get_google_data("1_zDRbDQ3KXl8aiFNkEuOsKLIlKwRc8bD4fyVHguMKI4")

# Al final, para el prompt:
final_text = build_master_prompt(datos_editados)
st.code(final_text)
