import streamlit as st

def app_arquitecto_sesiones():
    st.title("🏗️ Arquitecto de Sesiones PPT")
    st.subheader("Generador de Prompt Maestro para Gemini")

    # 1. Configuración de Contexto y Audiencia
    with st.expander("📂 Contexto, Público y Estructura", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            publico = st.text_input("¿Quién es el público?", placeholder="Ej. Gerentes, Dueños de empresa...")
            num_slides = st.number_input("Cantidad de Diapositivas", min_value=2, value=12)
        with col2:
            modulo_num = st.number_input("Número de Módulo", min_value=0, value=4)
            enfoque = st.text_input("Enfoque de la Sesión", placeholder="Ej. Liderazgo, Negociación, etc.")
        
        vinculo_curricular = st.text_area("Vínculo con otros módulos", 
                                          placeholder="Ej. Conectar con el tema X visto en el módulo anterior...")

    # 2. Instrucciones Específicas de Narrativa (EL GUION)
    st.write("### 🎯 Guion y Estructura Detallada")
    guion_especifico = st.text_area("Instrucciones por Slide / Cómo vincular los textos", 
                                    height=150,
                                    placeholder="Ej. Slide 1-3: Marco legal del Texto 1. Slide 4: El conflicto del Texto 2. Vincula el Texto 1 con el 2 usando el concepto de...")

    # 3. Entrada de Materia Prima
    st.write("### 📖 Materia Prima")
    t1 = st.text_area("Texto Principal (Copia y pega aquí)", height=200)
    t2 = st.text_area("Texto Secundario (Opcional)", height=150)
    
    # 4. Generación del Prompt Maestro
    if st.button("🚀 Generar Prompt para Gemini"):
        if not t1 or not enfoque:
            st.warning("Falta el texto principal o el enfoque de la sesión.")
        else:
            prompt_final = f"""
Actúa como un experto en diseño instruccional de alto nivel. 
Tu tarea es redactar el contenido para una presentación de exactamente {num_slides} diapositivas.

CONTEXTO:
- Público: {publico}
- Enfoque: {enfoque}
- Vínculo Curricular: {vinculo_curricular}

GUION E INSTRUCCIONES DE ESTRUCTURA:
{guion_especifico}

REGLAS DE ORO (STRICT):
1. IDIOMA: Todo en español técnico. Prohibido términos en inglés.
2. SIN RELLENO: Nada de introducciones vacías o frases de cortesía.
3. PROSA CON RITMO: El contenido de cada slide debe ser un texto fluido, profesional, provocador y CONCRETO. NADA DE VIÑETAS (BULLETS).
4. FIDELIDAD TÉCNICA: Usa definiciones precisas de los textos. Respeta la terminología original.
5. DINÁMICA ÚNICA: La diapositiva {num_slides} es EXCLUSIVAMENTE una dinámica práctica basada en la materia prima.

MATERIA PRIMA:
---
TEXTO 1:
{t1}
---
TEXTO 2:
{t2}
---

FORMATO DE SALIDA:
Entrega una lista numerada del 1 al {num_slides}.
Slides 1 a la {num_slides - 1}: Título y Texto de la Slide (Prosa con ritmo y concreta).
Slide {num_slides}: Título 'Dinámica Práctica' y descripción detallada.
            """
            
            st.success("¡Prompt generado! Cópialo para Gemini:")
            st.text_area("Prompt para copiar:", value=prompt_final, height=500)
