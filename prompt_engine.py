def build_master_prompt(contenido, avatar, configuracion, notas_extra):
    """
    CEREBRO UC: Generador de Prompt Maestro.
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

    # 2. CONTEXTO SISTEMA (Ajustado: Tono dinámico basado en Avatar)
    contexto_sistema = (
        f"Eres un estratega senior de 'Unidad Consciente'. Tu especialidad es el neuro-liderazgo. "
        f"Tu tono debe adaptarse al lenguaje de: {avatar['Tipo de Lenguaje']}."
    )

    # 3. CONSTRUCCIÓN DEL PROMPT
    return f"""
{contexto_sistema}

REGLAS DE ORO DE ESCRITURA (ESTRICTO):
1. ABSTRACCIÓN DEL AVATAR: El nombre del perfil es solo una referencia interna. PROHIBIDO usar nombres propios en el contenido final. Dirígete a la psicología y situación del cargo, no a una persona llamada {avatar['Nombre']}.
2. FLUIDEZ ESTRATÉGICA: No anuncies las partes de la estrategia. Evita frases como "según la metodología" o "haciendo un merge". El texto debe ser fluido.
3. CTA ÉPICO: No copies literal la columna CTA. Úsala como base para crear una invitación inspiradora y de alto nivel.
4. EVOCACIÓN BIOLÓGICA: No repitas la hormona como un dato técnico. Usa palabras y conceptos que PROVOQUEN el estado de {avatar['Hormona']} en el lector.
5. INVESTIGACIÓN DE ARCHIVOS: No menciones el nombre de los archivos (como .docx o .pdf) en el texto. Extrae su sabiduría y úsala para que el output sea profesional y profundo.

ESTRUCTURA DE REFERENCIA:
- Molde Narrativo: 01_Estructura_Narrativa.docx
- Teoría de Liderazgo: {tema1_nombre} (Basado en {file_t1})
- Teoría Biológica: {tema2_nombre} (Basado en {file_t2})

MATERIA PRIMA:
- Cargo/Perfil: {avatar['Nombre']} | Edad: {avatar['Edad']}
- Conflicto: {avatar['Incongruencia (El Conflicto)']}
- Necesidad: {avatar['Necesidad (CNV)']}
- Palabra Clave: {avatar['Palabra Clave (Sally)']}
- Villano: {avatar['Villano']} | Metamensaje: {avatar['Metamensaje']}

ESTRATEGIA:
- Objetivo: {contenido['Objetivo']}
- Formato: {contenido['Formato']}
- Problema: {contenido['Problema (Situación)']}
- El Merge: {contenido['El Merge (Línea Narrativa)']}
- Resultado: {contenido['Resultado']}
- CTA BASE: {contenido['CTA']}

TAREA:
Genera 5 propuestas de {contenido['Formato']} aplicando la investigación profunda de los archivos y respetando las reglas de escritura. 

NOTAS EXTRA: {notas_extra if notas_extra else "Sin notas adicionales."}
"""
