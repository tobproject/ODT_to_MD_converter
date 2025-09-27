# ODT TO MD CONVERTER


#### Feel free to contact me through the following profiles:

 ## [Linkedin](https://www.linkedin.com/in/andrespds/) | [GitHub](https://github.com/tobproject) | [Instagram](https://www.instagram.com/tob_project/)

---

## Description

This script converts files with the `.odt` (OpenDocument Text) extension to Markdown (`.md`) files, automatically adding the creation date in YAML format for easier use on platforms like GitBook. It also allows you to insert custom HTML styles into the resulting Markdown to improve the visual formatting.

---

## Features

- Converts ODT files to Markdown with high fidelity using Pandoc.
- Adds YAML frontmatter with the file's creation date for display in GitBook or other systems.
- Allows you to insert HTML tags to customize styles within Markdown.
- Easy to use and modify to adapt to different documentation workflows.

---

## Project Structure

### Feel free to contact me through the following profiles:
├── odt_to_md_converter.py # Script principal para conversión y formateo
├── README.md # Este archivo
├── examples/ # Carpeta con archivos de ejemplo (.odt y .md)




---

## Requirements

- Python 3.x  
- Pandoc instalado y agregado al PATH del sistema  
- Librería Python `pypandoc` (instalable con `pip install pypandoc`)

---

## Installation

## 1. Clona el repositorio o descarga el script:  

```
https://github.com/tobproject/ODT_to_MD_converter.git

cd odt-to-markdown
```


## 2. Instala la librería `pypandoc`:  


## 3. Instala Pandoc siguiendo las instrucciones oficiales:  
[https://pandoc.org/installing.html](https://pandoc.org/installing.html)

## 4. Verifica la instalación ejecutando en consola:  

---

## Usage

# 1. Modifica las variables 
```ruta_odt```  y  ```ruta_md``` en el script ```convertir_odt_a_md.py``` para apuntar a tus archivos.  

# 2. Ejecuta el script:  
El script realizará:  
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



