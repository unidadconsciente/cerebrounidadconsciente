def build_master_prompt(d):
    return f"""
Actúa como estratega de Bio-Liderazgo.
OBJETIVO: {d['objetivo']}
TEMAS: {d['tema1']} (Ref: {d['file1']}) y {d['tema2']} (Ref: {d['file2']})
MERGE: {d['merge']}
SOBERANÍA: {d['soberania']}
"""
