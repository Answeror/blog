from flask import current_app, render_template_string
from fn.iters import takewhile, dropwhile
import datetime
import yaml
import os


def get_arts():
    def gen():
        for name in os.listdir(art_root()):
            name, ext = os.path.splitext(name)
            if not name.startswith('.'):
                yield Art.load(name)

    return sorted(gen(), reverse=True, key=lambda a: a.ctime)


def art_root():
    return current_app.config.get('ART_ROOT', 'arts')


class Art(object):

    def __init__(self, name, path, text, hint):
        self.name = name
        self.path = path

        lines = text.split('\n')

        self.head = yaml.load('\n'.join(takewhile(lambda s: s.strip(), lines)))
        if 'type' not in self.head:
            self.head['type'] = hint

        self.raw = '\n'.join(
            dropwhile(
                lambda s: not s.strip(),
                dropwhile(lambda s: s.strip(), lines)
            )
        )

    @property
    def id(self):
        return self.name

    @property
    def title(self):
        return self.head['title']

    @property
    def ctime(self):
        time = self.head.get('ctime', None)
        if time is None:
            time = self.head.get('time', None)
        if time is None:
            time = self.head['date']

        if isinstance(time, datetime.datetime):
            return time

        if isinstance(time, datetime.date):
            return datetime.datetime.combine(time, datetime.time(0, 0, 0))

        for fmt in [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M',
            '%Y-%m-%d'
        ]:
            try:
                return datetime.datetime.strptime(time.strip(), fmt)
            except:
                pass

    @property
    def type(self):
        return self.head['type']

    @property
    def body(self):
        return self.render()

    def render(self):
        return getattr(self, '_render_' + self.type)()

    def _render_markdown(self):
        import markdown
        import pygments
        assert pygments
        extensions = [
            'codehilite',
            'fenced_code',
            'def_list',
            'attr_list',
            'footnotes'
        ]
        return markdown.markdown(render_template_string(self.raw), extensions)

    def _render_jinja2(self):
        return render_template_string(self.raw)

    @classmethod
    def load(cls, name):
        for ext, hint in [
            ('', None),
            ('.md', 'markdown'),
            ('.html', 'html')
        ]:
            path = os.path.join(art_root(), name + ext)
            if os.path.exists(path):
                break
        else:
            raise Exception('no art named ' + name)

        with open(path, 'rb') as f:
            text = f.read().decode('utf-8')
        return cls(name, path, text, hint)

    @property
    def show_head(self):
        return self.head.get('show_head', True)
