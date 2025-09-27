
```markdown
# ODT TO MD CONVERTER

 ## [Linkedin](https://www.linkedin.com/in/andrespds/) | [GitHub](https://github.com/tobproject) | [Instagram](https://www.instagram.com/tob_project/)


---

## Description

Este script convierte archivos con extensión `.odt` (OpenDocument Text) a archivos Markdown (`.md`), añadiendo automáticamente la fecha de creación en formato YAML para facilitar su uso en plataformas como GitBook. Además, permite insertar estilos HTML personalizados en el Markdown resultante para mejorar el formato visual.

---

## Features

- Convierte archivos ODT a Markdown con alta fidelidad usando Pandoc.  
- Añade frontmatter YAML con la fecha de creación del archivo para mostrarla en GitBook u otros sistemas.  
- Permite insertar etiquetas HTML para personalizar estilos dentro del Markdown.  
- Fácil de usar y modificar para adaptarse a distintos flujos de trabajo de documentación.

---

## Project Structure

```

├── convertir_odt_a_md.py    \# Script principal para conversión y formateo
├── README.md                \# Este archivo
├── ejemplos/                \# Carpeta con archivos de ejemplo (.odt y .md)

```

---

## Requirements

- Python 3.x  
- Pandoc instalado y agregado al PATH del sistema  
- Librería Python `pypandoc` (instalable con `pip install pypandoc`)

---

## Installation

1. Clona el repositorio o descarga el script:  

```

git clone https://github.com/tobproject/odt-to-markdown.git
cd odt-to-markdown

```

2. Instala la librería `pypandoc`:  

```

pip install pypandoc

```

3. Instala Pandoc siguiendo las instrucciones oficiales:  
https://pandoc.org/installing.html

4. Verifica la instalación ejecutando en consola:  

```

pandoc --version

```

---

## Usage

1. Modifica las variables `ruta_odt` y `ruta_md` en el script `convertir_odt_a_md.py` para apuntar a tus archivos.  

2. Ejecuta el script:  

```

python convertir_odt_a_md.py

```

3. El script realizará:  
   - Conversión del archivo `.odt` a `.md`.  
   - Inserción de la fecha de creación en formato YAML al inicio del Markdown.  
   - Reemplazo de títulos por HTML con estilos personalizados (configurable).

---

## License

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---

## Contact

Para dudas o sugerencias, puedes contactarme a través de [tu email o perfil GitHub].

---

¡Gracias por usar este conversor ODT a Markdown! 🚀
```


---

¿Quieres que te ayude a generar también un archivo LICENSE o a preparar ejemplos de uso para tu repositorio?

