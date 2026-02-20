def build_master_prompt(contenido, avatar, configuracion, notas_extra):
    """
    CEREBRO UC: Generador de Prompt Maestro con Auditoría, Moldes Dinámicos y CTA.
    """
    
    # 1. BÚSQUEDA DE ARCHIVOS TÉCNICOS
    tema1_nombre = contenido['Tema 1 (Liderazgo)']
    tema2_nombre = contenido['Tema 2 (Bio)']
    
    try:
        file_t1 = configuracion[configuracion['Tema'] == tema1_nombre]['File'].values[0]
    except:
        file_t1 = "ARCHIVO_NO_DEFINIDO"
        
    try:
        file_t2 = configuracion[configuracion['Tema'] == tema2_nombre]['File'].values[0]
    except:
        file_t2 = "ARCHIVO_NO_DEFINIDO"

    # 2. DEFINICIÓN DE MOLDES POR FORMATO
    templates = {
        "Video": """
TAREA: Genera un GUION ESTRATÉGICO para Video Corto (Reel/TikTok).
- ESTRUCTURA: [Tiempo] | [Visual/Toma sugerida] | [Voz en Off / Texto].
- REGLA DE ORO: El gancho visual debe ocurrir en los primeros 1.5 segundos.
- CIERRE: CTA visual y auditivo simultáneo basado en: {contenido['CTA']}.""",

        "Post": """
TAREA: Redacta un POST de una sola diapositiva / Frase corta.
- FORMATO: Una sola frase corta, potente y motivadora que encapsule la esencia del Merge.
- REGLA DE ORO: Debe ser 'sharable'. Que el avatar quiera postearla en sus historias.
- CIERRE: Incluye de forma sutil el CTA: {contenido['CTA']}.""",

        "Carrousel": """
TAREA: Diseña una ESTRUCTURA DE CARRUSEL (7-10 láminas).
- LÁMINA 1: Portada con el Hook más disruptivo.
- LÁMINAS 2-6: Desarrollo narrativo uniendo los temas técnicos y el Merge.
- LÁMINA FINAL: CTA de cierre. Puedes usar o mejorar creativamente este: {contenido['CTA']}.""",

        "Trivia": """
TAREA: Crea una TRIVIA DE VALIDACIÓN (4 preguntas).
- REGLA DE ORO: No deben ser ni muy fáciles ni muy difíciles. El usuario debe sentirse inteligente al responder, pero cuestionado en su incongruencia.
- ESTRUCTURA: Pregunta, 3 opciones y una 'Explicación Maestra' que valide el acierto del usuario usando los textos técnicos."""
    }

    # Selección del molde basado en el formato
    instruccion_formato = templates.get(contenido['Formato'], templates["Post"])

    # 3. CONTEXTO SISTEMA
    contexto_sistema = f"""
Eres un estratega senior de 'Unidad Consciente'. Experto en marketing y meditación profunda.
Tu tono debe ser directo, crítico y alineado al lenguaje de: {avatar['Tipo de Lenguaje']}.

⚠️ PROTOCOLO DE AUDITORÍA:
1. Lee el 100% de {file_t1} y {file_t2}.
2. Integra la ingeniería de '01_Estructura_Narrativa.docx'.
3. Antes de las propuestas, detalla un punto clave que aprendiste de cada archivo técnico.
"""

    # 4. ENSAMBLE FINAL CON COLUMNA CTA
    return f"""
{contexto_sistema}

{instruccion_formato}

REGLAS DE ESCRITURA (ESTRICTAS):
1. ABSTRACCIÓN: Habla a la psicología y cargo del avatar, nunca uses su nombre.
2. BIOLOGÍA: Provoca la liberación de {avatar['Hormona']} mediante el ritmo y peso de las palabras.
3. PROHIBICIÓN: Prohibido usar 'Soberanía' o derivados.
4. CONCISIÓN: Texto punchy.

ESTRATEGIA TÉCNICA:
- TEMA 1: {tema1_nombre} ({file_t1})
- TEMA 2: {tema2_nombre} ({file_t2})
- LÍNEA NARRATIVA: {contenido['El Merge (Línea Narrativa)']}

RADIOGRAFÍA DEL AVATAR:
- Villano: {avatar['Villano']}
- Incongruencia: {avatar['Incongruencia (El Conflicto)']}
- Metamensaje: {avatar['Metamensaje']}
- Problema actual: {contenido['Problema (Situación)']}
- Deseo: {contenido['Deseo']}
- Resultado Final: {contenido['Resultado']}
- CTA BASE: {contenido['CTA']}

NOTAS EXTRA: {notas_extra if notas_extra else "Sin notas adicionales."}
"""
