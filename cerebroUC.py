import streamlit as st
from data_engine import get_google_data
from prompt_engine import build_master_prompt
from promt_ppts import app_arquitecto_sesiones

st.set_page_config(page_title="Cerebro UC - Matriz de Control", layout="wide")

# Carga de datos
avatar, contenido, configuracion = get_google_data()


#Pestañas
# --- ESTRUCTURA DE PESTAÑAS ---
tab_matriz, tab_ppts = st.tabs(["📊 Matriz de Control", "🏗️ Arquitecto de Sesiones"])

with tab_matriz:
    st.title("🧠 Matriz de Control: Unidad Consciente")
    st.markdown("---")

# SELECTOR MAESTRO
semanas = contenido['Semana'].unique()
semana_sel = st.selectbox("📅 Selecciona la Semana de Trabajo:", semanas)

# Filtrado de fila de contenido
fila_c = contenido[contenido['Semana'] == semana_sel].iloc[0]

# Búsqueda automática del Avatar correspondiente
fila_a = avatar[avatar['Nombre'] == fila_c['Avatar']].iloc[0]

# MATRIZ VISUAL DE EDICIÓN
col1, col2, col3 = st.columns([1, 1, 1.2])

with col1:
    st.subheader("👤 Perfil del Avatar")
    # Mostramos datos clave para que ella verifique
    st.info(f"**Nombre:** {fila_a['Nombre']}\n\n**Hormona:** {fila_a['Hormona']}\n\n**Villano:** {fila_a['Villano']}")
    st.write(f"**Conflicto:** {fila_a['Incongruencia (El Conflicto)']}")

with col2:
    st.subheader("🎯 Estrategia de Contenido")
    # Campos editables por si quiere ajustar algo antes de generar
    formato = st.text_input("Formato", value=fila_c['Formato'])
    objetivo = st.text_input("Objetivo", value=fila_c['Objetivo'])
    problema = st.text_area("Problema (Situación)", value=fila_c['Problema (Situación)'])

with col3:
    st.subheader("🔗 Lógica del Merge")
    merge = st.text_area("Línea Narrativa (El Merge)", value=fila_c['El Merge (Línea Narrativa)'])
    deseo = st.text_input("Deseo", value=fila_c['Deseo'])
    resultado = st.text_input("Resultado", value=fila_c['Resultado'])

st.markdown("---")

# SECCIÓN DE ARCHIVOS (Validación de Config_Archivos)
st.subheader("📂 Verificación de Fuentes Técnicas")
c_f1, c_f2 = st.columns(2)

with c_f1:
    t1 = fila_c['Tema 1 (Liderazgo)']
    st.write(f"**Tema 1:** {t1}")
    # Visualización de la ruta que encontrará la def build_prompt
    f1_match = configuracion[configuracion['Tema'] == t1]['File']
    st.code(f1_match.values[0] if not f1_match.empty else "❌ Sin archivo en Config_Archivos")

with c_f2:
    t2 = fila_c['Tema 2 (Bio)']
    st.write(f"**Tema 2:** {t2}")
    f2_match = configuracion[configuracion['Tema'] == t2]['File']
    st.code(f2_match.values[0] if not f2_match.empty else "❌ Sin archivo en Config_Archivos")

# ENTRADA DE NOTAS Y ACCIÓN
notas_extra = st.text_area("✍️ Notas adicionales para este prompt (ej. Tono específico, contexto de hoy):")

if st.button("🚀 GENERAR PROMPT MAESTRO"):
    # Actualizamos la fila de contenido con lo que se editó en la interfaz
    fila_c_editada = fila_c.copy()
    fila_c_editada['Formato'] = formato
    fila_c_editada['Objetivo'] = objetivo
    fila_c_editada['Problema (Situación)'] = problema
    fila_c_editada['El Merge (Línea Narrativa)'] = merge
    fila_c_editada['Deseo'] = deseo
    fila_c_editada['Resultado'] = resultado
    
    # Llamada al cerebro (build_prompt ya hace el cruce interno con configuracion)
    prompt_final = build_master_prompt(fila_c_editada, fila_a, configuracion, notas_extra)
    
    st.success("Prompt generado con éxito. Cópialo y pégalo en el Gemini de trabajo.")
    st.code(prompt_final, language="markdown")

# PESTAÑA 2: ARQUITECTO DE SESIONES (Llamada al módulo externo)
with tab_ppts:
    # LLAMAMOS A LA FUNCIÓN QUE IMPORTAMOS
    app_arquitecto_sesiones()()

