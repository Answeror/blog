from jinja2 import nodes
from jinja2.ext import Extension
from shpaml import convert_text


class Shpaml(Extension):

    tags = set(['shpaml'])

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(['name:endshpaml'], drop_needle=True)
        return nodes.CallBlock(
            self.call_method('_shpaml', []),
            [],
            [],
            body
        ).set_lineno(lineno)

    def _shpaml(self, caller):
        return convert_text(caller())
