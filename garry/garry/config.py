import os
import sys
from jinja2 import Environment, PackageLoader

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..")))

templates = Environment(loader=PackageLoader('garry', 'templates'))

XSL_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "xsl"))
XML_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "xml" ))
apply_xsl = True

execfile(os.path.join(os.path.dirname(__file__), 'config.cfg'))
