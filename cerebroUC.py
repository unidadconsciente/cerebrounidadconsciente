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
    
    # 1. NAVEGACIÓN
    c1, c2, c3 = st.columns(3)
    with c1:
        serie_sel = st.selectbox("📂 Serie:", contenido['Serie'].unique())
    with c2:
        semanas = contenido[contenido['Serie'] == serie_sel]['Semana'].unique()
        semana_sel = st.selectbox("📅 Semana:", semanas)
    with c3:
        filas = contenido[(contenido['Serie'] == serie_sel) & (contenido['Semana'] == semana_sel)]
        

    # Selección de fila de contenido y match con Avatar completo
    
    fila_a = avatar_df[avatar_df['Nombre'] == fila_c['Avatar']].iloc[0]

    st.markdown("---")

    # 2. COLUMNAS DE EDICIÓN
    col_a, col_b, col_c = st.columns([1, 1, 1.2])

    with col_a:
        st.subheader("👤 Perfil Psicográfico")
        st.info(f"**{fila_a['Nombre']}** | Edad: {fila_a['Edad']} | Hormona: {fila_a['Hormona']}")
        
        with st.expander("🧠 Núcleo del Conflicto", expanded=True):
            st.write(f"**Villano:** {fila_a['Villano']}")
            st.write(f"**Incongruencia:** {fila_a['Incongruencia (El Conflicto)']}")
            st.write(f"**Necesidad (CNV):** {fila_a['Necesidad (CNV)']}")
            st.write(f"**Metamensaje:** {fila_a['Metamensaje']}")

        with st.expander("🎭 Dinámica Sentimental", expanded=False):
            st.write(f"**Sentimiento Hoy:** {fila_a['Sentimiento Hoy']}")
            st.write(f"**Sentimiento que Quiere:** {fila_a['Sentimiento que Quiere']}")
            st.write(f"**Palabra Clave (Sally):** {fila_a['Palabra Clave (Sally)']}")
            st.write(f"**Tipo de Lenguaje:** {fila_a['Tipo de Lenguaje']}")

        with st.expander("⚡ Disparadores de Venta", expanded=False):
            st.warning(f"**Costo Inacción:** {fila_a['Costo Inacción']}")
            st.write(f"**Mecanismo Único:** {fila_a['Mecanismo Único']}")
            st.write(f"**Objeción Raíz:** {fila_a['Objeción Raíz']}")
            st.write(f"**Disparador:** {fila_a['Disparador']}")

        with st.expander("📚 Pilares de Contenido", expanded=False):
            st.write(f"**Temas Liderazgo:** {fila_a['Temas (liderazgo)']}")
            st.write(f"**Temas Bio:** {fila_a['Temas bio']}")

    with col_b:
        st.subheader("🎯 Estrategia")
        f_list = sorted(contenido['Formato'].unique().tolist())
        idx_f = f_list.index(fila_c['Formato']) if fila_c['Formato'] in f_list else 0
        formato = st.selectbox("Formato", f_list, index=idx_f)

        o_list = sorted(contenido['Objetivo_Serie'].unique().tolist())
        idx_o = o_list.index(fila_c['Objetivo_Serie']) if fila_c['Objetivo_Serie'] in o_list else 0
        obj_serie = st.selectbox("Objetivo_Serie", o_list, index=idx_o)

        problema = st.text_area("Problema (Situación)", value=fila_c['Problema (Situación)'])

    with col_c:
        st.subheader("🔗 Línea Narrativa")
        merge = st.text_area("El Merge (Línea Narrativa)", value=fila_c['El Merge (Línea Narrativa)'], height=150)
        deseo = st.text_input("Deseo", value=fila_c['Deseo'])
        resultado = st.text_input("Resultado", value=fila_c['Resultado'])

    st.markdown("---")
    
    # 3. VERIFICACIÓN DE FUENTES TÉCNICAS (Búsqueda en Config_Archivos)
    st.subheader("📂 Fuentes de Conocimiento (Textos)")
    col_t1, col_t2 = st.columns(2)

    with col_t1:
        t1 = fila_c['Tema 1 (Liderazgo)']
        match1 = configuracion[configuracion['Tema'] == t1]['File']
        f1 = match1.values[0] if not match1.empty else "ARCHIVO_NO_DEFINIDO"
        st.write(f"**Tema 1 (Liderazgo):** {t1}")
        st.caption(f"Archivo: {f1}")

    with col_t2:
        t2 = fila_c['Tema 2 (Bio)']
        match2 = configuracion[configuracion['Tema'] == t2]['File']
        f2 = match2.values[0] if not match2.empty else "ARCHIVO_NO_DEFINIDO"
        st.write(f"**Tema 2 (Bio):** {t2}")
        st.caption(f"Archivo: {f2}")

    
# 4. NOTAS EXTRAS Y ENFOQUE
# 4. NOTAS EXTRAS Y ENFOQUE
    st.markdown("### ✍️ Notas Extras y Enfoque Narrativo")
    
    # CAMBIO AQUÍ: Quitamos la búsqueda de la columna inexistente y ponemos un valor vacío o un placeholder
    notas_input = st.text_area(
        "Ajusta el enfoque o añade notas para el prompt:",
        value="", # Esto evita el KeyError porque ya no busca en el Excel
        placeholder="Escribe aquí el enfoque específico o notas adicionales...",
        height=100
    )

    st.markdown("---")

    # 5. ACCIÓN DE GENERACIÓN
    if st.button("🚀 GENERAR PROMPT MAESTRO"):
        fila_editada = fila_c.copy()
        fila_editada['Formato'] = formato
        fila_editada['Objetivo_Serie'] = obj_serie
        fila_editada['Problema (Situación)'] = problema
        fila_editada['El Merge (Línea Narrativa)'] = merge
        fila_editada['Deseo'] = deseo
        fila_editada['Resultado'] = resultado
        
        # Se envía notas_input que contiene el enfoque + notas manuales
        prompt = build_master_prompt(fila_editada, fila_a, configuracion, notas_input)
        st.success("¡Prompt Maestro Generado!")
        st.code(prompt, language="markdown")

with tab_ppts:
    app_arquitecto_sesiones()
