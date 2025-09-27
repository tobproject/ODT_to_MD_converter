import os
from datetime import datetime
import re
import pypandoc

def agregar_fecha_frontmatter(ruta_md):
    """Agrega la fecha de creación al principio del archivo Markdown en formato YAML frontmatter."""
    with open(ruta_md, 'r', encoding='utf-8') as f:
        contenido = f.read()

    fecha_creacion = datetime.fromtimestamp(os.path.getctime(ruta_md)).strftime('%Y-%m-%d')

    frontmatter = f"""---
date: {fecha_creacion}
---

"""

    if not contenido.startswith('---'):
        with open(ruta_md, 'w', encoding='utf-8') as f:
            f.write(frontmatter + contenido)


def convertir_odt_a_md(ruta_odt, ruta_md):
    """Convierte un archivo .odt a .md usando pypandoc, preservando enlaces, listas, tablas e imágenes."""
    try:
        # Usamos 'gfm' (GitHub Flavored Markdown) y opciones para evitar conversión de listas y tablas
        pypandoc.convert_file(
            ruta_odt,
            'gfm',
            outputfile=ruta_md,
            extra_args=['--wrap=none', '--atx-headers']  # Evita que Pandoc rompa líneas y fuerza headers con #
        )
        print(f"Convertido {ruta_odt} a {ruta_md}")
    except Exception as e:
        print(f"Error al convertir {ruta_odt}: {e}")


def aplicar_estilos_encabezados(md_path):
    """
    Reemplaza todos los encabezados Markdown por HTML con estilos según el nivel:
    # -> h1, ## -> h2, ### -> h3, etc.
    """
    estilos = {
        1: 'color: red; font-size: 2em;',
        2: 'color: blue; font-size: 1.5em;',
        3: 'color: green; font-size: 1.2em;',
        4: 'color: purple; font-size: 1em;',
        5: 'color: orange; font-size: 0.9em;',
        6: 'color: gray; font-size: 0.8em;'
    }

    with open(md_path, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    nuevas_lineas = []
    for linea in lineas:
        match = re.match(r'^(#{1,6})\s+(.*)', linea)
        if match:
            nivel = len(match.group(1))
            texto = match.group(2)
            estilo = estilos.get(nivel, '')
            nueva_linea = f'<h{nivel} style="{estilo}">{texto}</h{nivel}>\n'
            nuevas_lineas.append(nueva_linea)
        else:
            nuevas_lineas.append(linea)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(nuevas_lineas)

    print(f"Encabezados estilizados en {md_path}")


if __name__ == "__main__":
    carpeta_origen = os.path.dirname(os.path.abspath(__file__))  # Carpeta del script
    carpeta_destino = os.path.join(carpeta_origen, "examples")

    # Crear carpeta examples si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    # Recorrer todos los archivos .odt en la carpeta de origen
    for archivo in os.listdir(carpeta_origen):
        if archivo.lower().endswith(".odt"):
            ruta_odt = os.path.join(carpeta_origen, archivo)
            nombre_md = os.path.splitext(archivo)[0] + ".md"
            ruta_md = os.path.join(carpeta_destino, nombre_md)

            convertir_odt_a_md(ruta_odt, ruta_md)
            agregar_fecha_frontmatter(ruta_md)
            aplicar_estilos_encabezados(ruta_md)

    print("¡Conversión de todos los archivos .odt completada!")
