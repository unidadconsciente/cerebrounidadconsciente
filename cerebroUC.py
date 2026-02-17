import streamlit as st
from data_engine import get_google_data
from prompt_engine import build_master_prompt
from promt_ppts import app_arquitecto_sesiones

st.set_page_config(page_title="Cerebro UC - Matriz de Control", layout="wide")

# Carga de datos
avatar_df, contenido, configuracion = get_google_data()

tab_matriz, tab_ppts = st.tabs(["📊 Matriz de Control", "🏗️ Arquitecto de Sesiones"])

with tab_matriz:
    st.title("🧠 Matriz de Control: Unidad Consciente")
    
    # 1. NAVEGACIÓN (Columnas exactas: Semana, Día, Serie, Tipo de Contenido)
    c1, c2, c3 = st.columns(3)
    with c1:
        serie_sel = st.selectbox("📂 Serie:", contenido['Serie'].unique())
    with c2:
        semanas = contenido[contenido['Serie'] == serie_sel]['Semana'].unique()
        semana_sel = st.selectbox("📅 Semana:", semanas)
    with c3:
        filas = contenido[(contenido['Serie'] == serie_sel) & (contenido['Semana'] == semana_sel)]
        tipo_sel = st.radio("📍 Tipo de Contenido:", filas['Tipo de Contenido'].unique(), horizontal=True)

    # Selección de fila de contenido y match con Avatar completo
    fila_c = filas[filas['Tipo de Contenido'] == tipo_sel].iloc[0]
    # Extraemos el registro completo del avatar con sus 17 columnas
    fila_a = avatar_df[avatar_df['Nombre'] == fila_c['Avatar']].iloc[0]

    st.markdown("---")

    # 2. COLUMNAS DE EDICIÓN
    col_a, col_b, col_c = st.columns([1, 1, 1.2])

    with col_a:
        st.subheader("👤 Perfil Psicográfico")
        # Visualización de datos clave del avatar
        st.info(f"**{fila_a['Nombre']}** | {fila_a['Hormona']}")
        st.write(f"**Conflicto:** {fila_a['Incongruencia (El Conflicto)']}")
        st.write(f"**Villano:** {fila_a['Villano']}")
        st.write(f"**Costo Inacción:** {fila_a['Costo Inacción']}")

    with col_b:
        st.subheader("🎯 Estrategia")
        
        # Selectores dinámicos
        f_list = sorted(contenido['Formato'].unique().tolist())
        idx_f = f_list.index(fila_c['Formato']) if fila_c['Formato'] in f_list else 0
        formato = st.selectbox("Formato", f_list, index=idx_f)

        o_list = sorted(contenido['Objetivo_Serie'].unique().tolist())
        idx_o = o_list.index(fila_c['Objetivo_Serie']) if fila_c['Objetivo_Serie'] in o_list else 0
        obj_serie = st.selectbox("Objetivo_Serie", o_list, index=idx_o)

        problema = st.text_area("Problema (Situación)", value=fila_c['Problema (Situación)'])

    with col_c:
        st.subheader("🔗 Línea Narrativa")
        merge = st.text_area("El Merge (Línea Narrativa)", value=fila_c['El Merge (Línea Narrativa)'])
        deseo = st.text_input("Deseo", value=fila_c['Deseo'])
        resultado = st.text_input("Resultado", value=fila_c['Resultado'])

    # 3. ACCIÓN DE GENERACIÓN
    if st.button("🚀 GENERAR PROMPT MAESTRO"):
        # Creamos copias para no alterar el DataFrame original
        fila_editada = fila_c.copy()
        fila_editada['Formato'] = formato
        fila_editada['Objetivo_Serie'] = obj_serie
        fila_editada['Problema (Situación)'] = problema
        fila_editada['El Merge (Línea Narrativa)'] = merge
        fila_editada['Deseo'] = deseo
        fila_editada['Resultado'] = resultado
        
        # Pasamos la fila del avatar completa (con las 17 columnas) al motor
        prompt = build_master_prompt(fila_editada, fila_a, configuracion, fila_c['Enfoque Narrativo / Pregunta Trivia'])
        st.code(prompt, language="markdown")

with tab_ppts:
    app_arquitecto_sesiones()
