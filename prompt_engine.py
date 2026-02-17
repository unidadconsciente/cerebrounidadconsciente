def build_master_prompt(contenido, avatar, configuracion, notas_extra):
    """
    CEREBRO UC: Generador de Prompt Maestro con Inteligencia de Serie y Estructura Tidy.
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

    # 2. CONTEXTO SISTEMA
    contexto_sistema = (
        f"Eres un estratega senior de 'Unidad Consciente'. Tu especialidad es el neuro-liderazgo. "
        f"Tu tono debe adaptarse al lenguaje de: {avatar['Tipo de Lenguaje']}."
    )

    # 3. CONSTRUCCIÓN DEL PROMPT
    return f"""
{contexto_sistema}

REGLAS DE ORO DE ESCRITURA (ESTRICTO):
1. ABSTRACCIÓN DEL AVATAR: Prohibido usar nombres propios. Dirígete a la psicología y cargo del avatar.
2. FLUIDEZ ESTRATÉGICA: Sin anuncios de metodología o fases. El texto debe ser fluido y orgánico.
3. CTA ÉPICO: Crea una invitación inspiradora basada en el objetivo, no copies literal el CTA.
4. EVOCACIÓN BIOLÓGICA: Provoca la liberación de {avatar['Hormona']} en el lector a través de las palabras, no menciones la hormona.
5. NO SOBERANÍA: Prohibido usar 'soberano', 'soberanía' o derivados. Demuéstralo con el lenguaje.
6. CONCISIÓN: Texto punchy. Usa las reglas de hooks de '01_Estructura_Narrativa.docx'.

ESTRUCTURA DE REFERENCIA:
- Molde Narrativo: 01_Estructura_Narrativa.docx
- Teoría de Liderazgo: {tema1_nombre} (vía {file_t1})
- Teoría Biológica: {tema2_nombre} (vía {file_t2})

CONTEXTO ESTRATÉGICO DE LA SERIE:
- Serie Actual: {contenido['Serie']}
- Etapa de Campaña: {contenido['Objetivo_Serie']}
- Paso Narrativo: {contenido['Paso (1-4)']} de 4
- Tipo de Contenido: {contenido['Tipo de Contenido']}

MATERIA PRIMA:
- Perfil: {avatar['Nombre']} | Edad: {avatar['Edad']}
- Conflicto: {avatar['Incongruencia (El Conflicto)']}
- Villano: {avatar['Villano']} | Metamensaje: {avatar['Metamensaje']}
- Enfoque Específico: {contenido['Enfoque Narrativo / Pregunta Trivia']}

ESTRATEGIA EDITADA:
- Objetivo: {contenido['Objetivo']}
- Formato: {contenido['Formato']}
- Problema (Situación): {contenido['Problema (Situación)']}
- El Merge: {contenido['El Merge (Línea Narrativa)']}
- Deseo: {contenido['Deseo']}
- Resultado: {contenido['Resultado']}

TAREA:
Genera 5 propuestas creativas para este {contenido['Formato']}. 
Si es 'Post', profundiza en la integración técnica de los archivos. 
Si es 'Trivia', genera una interacción de alto impacto que valide el problema del avatar.

NOTAS EXTRA: {notas_extra if notas_extra else "Sin notas adicionales."}
"""
