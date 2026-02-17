import streamlit as st
from data_engine import get_google_data
from prompt_engine import build_master_prompt
from promt_ppts import app_arquitecto_sesiones

st.set_page_config(page_title="Cerebro UC - Matriz de Control", layout="wide")

# Carga de datos (get_google_data ahora retorna 4 elementos)
avatar, contenido, configuracion, opciones = get_google_data()

tab_matriz, tab_ppts = st.tabs(["📊 Matriz de Control", "🏗️ Arquitecto de Sesiones"])

with tab_matriz:
    st.title("🧠 Matriz de Control: Unidad Consciente")
    st.markdown("---")

    # --- SISTEMA DE FILTRADO SIDEBAR ---
    st.sidebar.header("🎯 Navegación Estratégica")
    
    # 1. Selección por Serie
    series_disponibles = contenido['Serie'].unique()
    serie_sel = st.sidebar.selectbox("📂 Selecciona la Serie:", series_disponibles)

    # 2. Selección por Semana (filtrada por serie)
    semanas_serie = contenido[contenido['Serie'] == serie_sel]['Semana'].unique()
    semana_sel = st.sidebar.selectbox("📅 Selecciona la Semana:", semanas_serie)

    # 3. Selección Tipo de Contenido (Post vs Trivia)
    filas_match = contenido[(contenido['Serie'] == serie_sel) & (contenido['Semana'] == semana_sel)]
    tipo_sel = st.radio("📍 Tipo de Contenido:", filas_match['Tipo de Contenido'].unique(), horizontal=True)

    # Fila final de contenido y búsqueda de Avatar
    fila_c = filas_match[filas_match['Tipo de Contenido'] == tipo_sel].iloc[0]
    fila_a = avatar[avatar['Nombre'] == fila_c['Avatar']].iloc[0]

    # --- MATRIZ VISUAL DE EDICIÓN ---
    col1, col2, col3 = st.columns([1, 1, 1.2])

    with col1:
        st.subheader("👤 Perfil del Avatar")
        st.info(f"**Nombre:** {fila_a['Nombre']}\n\n**Hormona:** {fila_a['Hormona']}\n\n**Villano:** {fila_a['Villano']}")
        st.write(f"**Conflicto:** {fila_a['Incongruencia (El Conflicto)']}")

    with col2:
        st.subheader("🎯 Estrategia")
        
        # Selectores Dinámicos (Botones precargados desde Config_Opciones)
        lista_formatos = opciones['Formato'].dropna().tolist()
        idx_f = lista_formatos.index(fila_c['Formato']) if fila_c['Formato'] in lista_formatos else 0
        formato = st.selectbox("Formato", lista_formatos, index=idx_f)

        lista_objs = opciones['Objetivo_Serie'].dropna().tolist()
        idx_o = lista_objs.index(fila_c['Objetivo_Serie']) if fila_c['Objetivo_Serie'] in lista_objs else 0
        obj_serie = st.selectbox("Objetivo Serie", lista_objs, index=idx_o)

        objetivo = st.text_input("Objetivo Específico", value=fila_c['Objetivo'])
        problema = st.text_area("Problema (Situación)", value=fila_c['Problema (Situación)'])

    with col3:
        st.subheader("🔗 Lógica del Merge")
        merge = st.text_area("Línea Narrativa (El Merge)", value=fila_c['El Merge (Línea Narrativa)'])
        deseo = st.text_input("Deseo", value=fila_c['Deseo'])
        resultado = st.text_input("Resultado", value=fila_c['Resultado'])

    st.markdown("---")

    # --- VERIFICACIÓN DE FUENTES ---
    st.subheader("📂 Verificación de Fuentes Técnicas")
    c_f1, c_f2 = st.columns(2)

    with c_f1:
        t1 = fila_c['Tema 1 (Liderazgo)']
        st.write(f"**Tema 1:** {t1}")
        f1_match = configuracion[configuracion['Tema'] == t1]['File']
        st.code(f1_match.values[0] if not f1_match.empty else "❌ Sin archivo")

    with c_f2:
        t2 = fila_c['Tema 2 (Bio)']
        st.write(f"**Tema 2:** {t2}")
        f2_match = configuracion[configuracion['Tema'] == t2]['File']
        st.code(f2_match.values[0] if not f2_match.empty else "❌ Sin archivo")

    notas_extra = st.text_area("✍️ Notas adicionales para este prompt:", key="matriz_notas")

    if st.button("🚀 GENERAR PROMPT MAESTRO"):
        fila_c_editada = fila_c.copy()
        fila_c_editada['Formato'] = formato
        fila_c_editada['Objetivo_Serie'] = obj_serie
        fila_c_editada['Objetivo'] = objetivo
        fila_c_editada['Problema (Situación)'] = problema
        fila_c_editada['El Merge (Línea Narrativa)'] = merge
        fila_c_editada['Deseo'] = deseo
        fila_c_editada['Resultado'] = resultado
        
        prompt_final = build_master_prompt(fila_c_editada, fila_a, configuracion, notas_extra)
        st.success("Prompt generado con éxito.")
        st.code(prompt_final, language="markdown")

with tab_ppts:
    app_arquitecto_sesiones()
