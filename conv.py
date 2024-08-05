import bibtexparser
import os

# Ruta del archivo .bib
bib_file = 'my-hugo-site/data/bib/publications.bib'
output_dir = 'my-hugo-site/content/publications'
# Verificar si el archivo .bib existe
if not os.path.isfile(bib_file):
    raise FileNotFoundError(f"The file {bib_file} does not exist.")

# Cargar el archivo .bib
with open(bib_file) as f:
    bib_database = bibtexparser.load(f)

# Asegurarse de que el directorio de salida exista
os.makedirs(output_dir, exist_ok=True)

# Procesar cada entrada
for entry in bib_database.entries:
    # Limpiar la URL de cualquier protocolo
    url = entry.get('url', '')
    if url.startswith('http://'):
        url = url[len('http://'):]
    elif url.startswith('https://'):
        url = url[len('https://'):]
    
    filename = f"{entry['ID']}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Crear el contenido Markdown
    content = f"""---
title: "{entry.get('title', 'No Title')}"
date: {entry.get('year', 'Unknown')}-01-01
authors: "{entry.get('author', 'Unknown')}"
publication: "{entry.get('journal', 'Unknown')}"
note: "{entry.get('note', '')}"

---

This is the content of the publication. It describes the research and findings.
"""
    
    # Guardar el archivo Markdown
    with open(filepath, 'w') as f:
        f.write(content)