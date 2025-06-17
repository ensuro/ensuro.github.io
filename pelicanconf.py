import os
import yaml
import shutil
from jinja2 import Environment, FileSystemLoader

AUTHOR = 'Ensuro'
SITENAME = 'Ensuro'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LINKS = ()
SOCIAL = ()

DIRECT_TEMPLATES = [] 
READERS = {"html": None}

yaml_path = os.path.join(PATH, "data", "input.yaml")
with open(yaml_path, encoding="utf-8") as f:
    site_data = yaml.safe_load(f)

JINJA_GLOBALS = {'data': site_data}

template_dir = "templates"
rendered_dir = os.path.join(PATH, "rendered")
os.makedirs(rendered_dir, exist_ok=True)

env = Environment(loader=FileSystemLoader(template_dir))
template_files = [
    f for f in os.listdir(template_dir)
    if f.endswith(".html") and f != "master.html"
]

for template_name in template_files:
    template = env.get_template(template_name)
    output = template.render(**site_data)
    output_path = os.path.join(rendered_dir, template_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

EXTRA_PATH_METADATA = {
    **{f"rendered/{name}": {"path": name} for name in template_files}
}

STATIC_PATHS = ['static', 'rendered', 'data']

def copy_static_dirs():
    src = os.path.join(PATH, "data", "input.yaml")
    dst = os.path.join(PATH, "static", "admin", "input.yaml")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)

copy_static_dirs()
