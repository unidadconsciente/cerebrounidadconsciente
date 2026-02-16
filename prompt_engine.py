def build_master_prompt(contenido, avatar, configuracion, notas_extra):
    """
    CEREBRO UC: Generador de Prompt Maestro.
    Fuerza el uso de la estructura narrativa de '01_Estructura_Narrativa.docx'.
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
        "Eres un estratega senior de 'Unidad Consciente'. Tu especialidad es el "
        "neuro-liderazgo. Tu tono es directo, técnico y soberano."
    )

    # 3. CONSTRUCCIÓN DEL PROMPT
    return f"""
{contexto_sistema}

REGLA DE ORO: 
Para redactar esta pieza DEBES seguir estrictamente la estructura paso a paso definida en el archivo: 
👉 **'01_Estructura_Narrativa.docx'**

1. MATERIA PRIMA ESTRATÉGICA (Avatar_nuevo):
- Persona: {avatar['Nombre']} | Edad: {avatar['Edad']}
- Conflicto: {avatar['Incongruencia (El Conflicto)']}
- Necesidad (CNV): {avatar['Necesidad (CNV)']}
- Hormona: {avatar['Hormona']} | Anclaje: {avatar['Palabra Clave (Sally)']}
- Villano: {avatar['Villano']} | Metamensaje: {avatar['Metamensaje']}

2. ESTRATEGIA DE LA PIEZA (Contenido):
- Objetivo: {contenido['Objetivo']}
- Formato: {contenido['Formato']}
- Problema: {contenido['Problema (Situación)']}
- El Merge: {contenido['El Merge (Línea Narrativa)']}
- Deseo: {contenido['Deseo']}
- Resultado: {contenido['Resultado']}
- CTA ORIGINAL: {contenido['CTA']}

3. FUNDAMENTOS TÉCNICOS (Config_Archivos):
Usa estos archivos para validar la teoría científica y profesional:
- Liderazgo: [{file_t1}] (Tema: {tema1_nombre})
- Biología: [{file_t2}] (Tema: {tema2_nombre})

4. DESTINO FINAL:
Lleva al lector desde el 'Problema' hasta el 'Resultado' prometido, usando el 'Merge' para conectar la solución biológica de [{file_t2}] con el desafío de liderazgo.

NOTAS EXTRA: {notas_extra if notas_extra else "Sin notas adicionales."}

TAREA: 
Escribe 5 propuestas de {contenido['Formato']} aplicando los datos anteriores dentro del molde de '01_Estructura_Narrativa.docx'.
Restricciones
1.ABSTRACCIÓN DEL AVATAR: El nombre del perfil (ej. Sofía) es solo una referencia para el sistema. Prohibido usar nombres propios en el contenido final. Habla a la psicología, al cargo y a la situación del avatar, no a su nombre.
2. FLUIDEZ ESTRATÉGICA: No anuncies las partes de la estrategia. Evita frases tipo "según la metodología" o "integrando el concepto". El texto debe ser fluido y orgánico
3. CTA ÉPICO: No copies literal la columna [CTA]. Úsala como base para crear una invitación inspiradora que conecte con el resultado de alto nivel que busca el perfil.
4. EVOCACIÓN BIOLÓGICA: No te limites a repetir el nombre de la hormona o el neurotransmisor de la tabla. Tu objetivo es usar palabras clave, metáforas y un estilo narrativo que "provoque" o "cree" ese estado químico en el lector. Puedes mencionar términos científicos si aportan valor, pero no como una lista de datos.
5. No digas "nombre del archivo"

Obligación: Realiza investigación profunda de los archvios en files, que el output sea profesional

"""
