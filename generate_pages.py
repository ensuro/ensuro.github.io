import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Cargar input.yaml desde content/data/
with open("content/data/input.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Configurar entorno de Jinja2 para templates/
env = Environment(loader=FileSystemLoader("templates"))

# Detectar todos los templates .html (excepto master.html)
templates = [
    f for f in os.listdir("templates")
    if f.endswith(".html") and f != "master.html"
]

# Crear carpeta content si no existe
os.makedirs("content", exist_ok=True)

# Renderizar templates
for template_name in templates:
    template = env.get_template(template_name)
    output = template.render(**data)
    output_path = os.path.join("content", template_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"✅ Rendered: {template_name} → content/{template_name}")
