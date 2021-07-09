from datetime import datetime
from os import getcwd
from os.path import abspath, join
import sys


# Core settings
extensions = [
    "releases",
    "sphinx.ext.autodoc",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build"]
default_role = "obj"

project = u"Lexicon"
year = datetime.now().year
copyright = u"%d Jeff Forcier" % year

# Ensure project directory is on PYTHONPATH for version, autodoc access
sys.path.insert(0, abspath(join(getcwd(), "..")))

# Enforce use of Alabaster (even on RTD) and configure it
html_theme = "alabaster"
html_theme_options = {
    "description": "Pythonic attribute/alias/etc dict subclasses",
    "github_user": "bitprophet",
    "github_repo": "lexicon",
}
html_sidebars = {"**": ["about.html", "navigation.html", "searchbox.html"]}

# Other extension configs
releases_github_path = "bitprophet/lexicon"
