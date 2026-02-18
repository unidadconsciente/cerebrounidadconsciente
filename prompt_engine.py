def build_master_prompt(contenido, avatar, configuracion, notas_extra):
    """
    CEREBRO UC: Generador de Prompt Maestro con Inteligencia de Serie .
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
        f"Eres un estratega senior de 'Unidad Consciente'. Tu especialidad es el marketing, meditas desde hace muchos años.
        Pero antes, confirma que leiste los textos, no des nada hasta confirmar que leiste los textos, di que leiste dee cada uno, después pregutna si puedes continuar"
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
7. el texto es para redes, asique no debe ser muy largo. EL CTA DEBE SER coherente con el objetivo, debe ser corto e inspirador, palabras clave, por ejemplo "Comenta x palabra para ser parte"
8. Hooks concisos, revisa bien 01_Estructura_Narrativa.docx, la sección hooks

ESTRUCTURA DE REFERENCIA:
- Molde Narrativo: 01_Estructura_Narrativa.docx

-Vas a encontrar puntos en comun en los temas, considera que es para hacer contendio para el avatar, investiga los textos que te doy, profunidiza en ellos y crea contenido que una de manera coherente y creeativa ambos temas, siguiendo la linea narrativa definida abajo
- TEMA 1: {tema1_nombre} (vía {file_t1})
- TEMA 2: {tema2_nombre} (vía {file_t2})

CONTEXTO ESTRATÉGICO DE LA SERIE:
- Serie Actual: {contenido['Serie']}
- Etapa de Campaña: {contenido['Objetivo_Serie']}

- Tipo de Contenido: {contenido['Tipo de Contenido']}

MATERIA PRIMA DEL AVATAR (Radiografía Completa):
- Perfil: {avatar['Nombre']} | Edad: {avatar['Edad']} | Tipo de Lenguaje: {avatar['Tipo de Lenguaje']}
- Núcleo Psicológico:
    * Villano: {avatar['Villano']}
    * Incongruencia (El Conflicto): {avatar['Incongruencia (El Conflicto)']}
    * Metamensaje: {avatar['Metamensaje']}
    * Necesidad (CNV): {avatar['Necesidad (CNV)']}
- Dinámica Emocional:
    * Sentimiento Hoy: {avatar['Sentimiento Hoy']}
    * Sentimiento que Quiere: {avatar['Sentimiento que Quiere']}
    * Palabra Clave (Sally): {avatar['Palabra Clave (Sally)']}
    * Hormona a segregar: {avatar['Hormona']}
- Estrategia de Conversión:
    * Costo Inacción: {avatar['Costo Inacción']}
    * Mecanismo Único: {avatar['Mecanismo Único']}
    * Objeción Raíz: {avatar['Objeción Raíz']}
    * Disparador: {avatar['Disparador']}


ESTRATEGIA EDITADA:
- Objetivo: {contenido['Objetivo_Serie']}
- Formato: {contenido['Formato']}
- Problema (Situación): {contenido['Problema (Situación)']}
- Linea Narrativa: {contenido['El Merge (Línea Narrativa)']}
- Deseo: {contenido['Deseo']}
- Resultado: {contenido['Resultado']}
- El resultado debe superar al deseo
TAREA:
Genera 10 propuestas creativas para este {contenido['Formato']}. siguiendo la estrucura de 01_Estructura_Narrativa.docx, leela a detalle
Si es 'Post', profundiza en la integración técnica de los archivos. 
Si es 'Trivia', genera una interacción de alto impacto que valide el problema del avatar.
La trivia es una serie de 4 pregutnas con respuestas de opcion múltiple, que sean simples de contestar pero no tanto, que hagan sentir al avatar inteligente, pero no le hagan romperse la cabeza pensando, se basan en los textos
Si es video, incluye propuestas de tomas e imágenes y musica que genere las emociones deseadas en el avatar 
Revisa la estructura de los posts en 01_Estructura_Narrativa.docx, ES DECIR, HAY UN ORDEN claro al construir el contenido.. revisalo bien, sin errores, Es hook, problema, solución, oferta, cta..
LEE LOS TEXTOS Y ANTES DE HACER EL CONTENIDO CONFIRMA QUE LEISTE EL MATERIAL QUE SE TE PIDIO A DETALLE
NOTAS EXTRA: {notas_extra if notas_extra else "Sin notas adicionales."}
"""
