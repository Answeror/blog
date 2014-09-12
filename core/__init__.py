from flask import Flask
from . import jinja_ext


class App(Flask):

    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions', []).append(jinja_ext.Shpaml)


app = App(__name__)


from . import views
assert views

import os
import subprocess as sp
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
sp.check_call([
    'lessc',
    os.path.join(CURRENT_PATH, 'static', 'style.less'),
    os.path.join(CURRENT_PATH, 'static', 'style.css')
])
