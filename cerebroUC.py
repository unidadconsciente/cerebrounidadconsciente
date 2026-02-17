import streamlit as st
from data_engine import get_google_data
from prompt_engine import build_master_prompt
from promt_ppts import app_arquitecto_sesiones

st.set_page_config(page_title="Cerebro UC - Matriz de Control", layout="wide")

# Carga de datos (data_engine debe retornar avatar, contenido, configuracion)
avatar, contenido, configuracion = get_google_data()

tab_matriz, tab_ppts = st.tabs(["📊 Matriz de Control", "🏗️ Arquitecto de Sesiones"])

with tab_matriz:
    st.title("🧠 Matriz de Control: Unidad Consciente")
    
    # Navegación horizontal (Diseño original)
    c1, c2, c3 = st.columns(3)
    with c1:
        serie_sel = st.selectbox("📂 Serie:", contenido['Serie'].unique())
    with c2:
        # Esto asegura que veas las 12 semanas de la serie elegida
        semanas = contenido[contenido['Serie'] == serie_sel]['Semana'].unique()
        semana_sel = st.selectbox("📅 Semana:", semanas)
    with c3:
        filas = contenido[(contenido['Serie'] == serie_sel) & (contenido['Semana'] == semana_sel)]
        tipo_sel = st.radio("📍 Tipo:", filas['Tipo de Contenido'].unique(), horizontal=True)

    fila_c = filas[filas['Tipo de Contenido'] == tipo_sel].iloc[0]
    fila_a = avatar[avatar['Nombre'] == fila_c['Avatar']].iloc[0]

    st.markdown("---")

    col_a, col_b, col_c = st.columns([1, 1, 1.2])

    with col_a:
        st.subheader("👤 Avatar")
        st.info(f"**{fila_a['Nombre']}**\n\n{fila_a['Hormona']}\n\n{fila_a['Villano']}")
        st.write(f"Conflicto: {fila_a['Incongruencia (El Conflicto)']}")

    with col_b:
        st.subheader("🎯 Estrategia")
        
        # Botones dinámicos extraídos directamente de la columna 'Formato' de contenido
        f_list = sorted(contenido['Formato'].unique().tolist())
        idx_f = f_list.index(fila_c['Formato']) if fila_c['Formato'] in f_list else 0
        formato = st.selectbox("Formato", f_list, index=idx_f)

        # Botones dinámicos extraídos directamente de la columna 'Objetivo_Serie' de contenido
        o_list = sorted(contenido['Objetivo_Serie'].unique().tolist())
        idx_o = o_list.index(fila_c['Objetivo_Serie']) if fila_c['Objetivo_Serie'] in o_list else 0
        obj_serie = st.selectbox("Objetivo Serie", o_list, index=idx_o)

        objetivo = st.text_input("Objetivo", value=fila_c['Objetivo'])
        problema = st.text_area("Problema", value=fila_c['Problema (Situación)'])

    with col_c:
        st.subheader("🔗 Merge")
        merge = st.text_area("Línea Narrativa", value=fila_c['El Merge (Línea Narrativa)'])
        deseo = st.text_input("Deseo", value=fila_c['Deseo'])
        resultado = st.text_input("Resultado", value=fila_c['Resultado'])

    if st.button("🚀 GENERAR PROMPT MAESTRO"):
        # Actualizamos la fila con los cambios de los selectbox/inputs
        fila_editada = fila_c.copy()
        fila_editada['Formato'] = formato
        fila_editada['Objetivo_Serie'] = obj_serie
        fila_editada['Objetivo'] = objetivo
        fila_editada['Problema (Situación)'] = problema
        fila_editada['El Merge (Línea Narrativa)'] = merge
        fila_editada['Deseo'] = deseo
        fila_editada['Resultado'] = resultado
        
        prompt = build_master_prompt(fila_editada, fila_a, configuracion, "")
        st.code(prompt, language="markdown")

with tab_ppts:
    app_arquitecto_sesiones()
