import os
import yaml
import glob
from pelican.plugins import webassets

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

JINJA_GLOBALS = site_data

PDFS_DIR = os.path.join(PATH, "pdfs")
pdf_files = glob.glob(os.path.join(PDFS_DIR, "*.pdf"))

EXTRA_PATH_METADATA = {
    **{f"pdfs/{os.path.basename(f)}": {"path": os.path.basename(f)} for f in pdf_files}
}

STATIC_PATHS = [
    'assets',
    'font',
    'images',
    'pdfs',
]

WEBASSETS_SOURCE_PATHS = ['content/assets']
PLUGINS = [webassets]

THEME = '.'
THEME_TEMPLATES_OVERRIDES = ['templates']
DIRECT_TEMPLATES = ['index', 'about', 'careers', 'contact', 'investors']