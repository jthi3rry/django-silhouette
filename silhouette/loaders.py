import re
from django import forms
from django.forms.forms import BoundField
from django.template.loader import select_template
from .apps import Silhouette
from .utils import normalize


class DefaultLoader(object):

    def __init__(self, theme, template_patterns):
        self.theme = theme
        self.patterns = template_patterns

    def get_substitutes(self, obj):
        if isinstance(obj, forms.Form):
            return {'theme': self.theme,
                    'form': normalize(type(obj).__name__)}
        elif isinstance(obj, BoundField):
            return {'theme': self.theme,
                    'form': normalize(type(obj.form).__name__),
                    'field': normalize(obj.name),
                    'widget': normalize(type(obj.field.widget).__name__)}
        raise ValueError("Object of type {} is not supported".format(type(obj)))

    def select_template(self, patterns, substitutes):
        template_list = [pattern.format(**substitutes) for pattern in patterns]
        return select_template(template_list)

    def get_template(self, template_type, obj):
        return self.select_template(self.patterns[template_type], self.get_substitutes(obj))

    def __call__(self, *args, **kwargs):
        return self.get_template(*args, **kwargs)


get_silhouette = loader = Silhouette.settings.LOADER(Silhouette.settings.THEME, Silhouette.settings.PATTERNS)
