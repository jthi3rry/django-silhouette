import re
from django.forms.forms import BaseForm, BoundField
from django.forms.formsets import BaseFormSet

from django.template.loader import select_template
from .apps import Silhouette
from .utils import normalize


class DefaultLoader(object):

    def get_substitutes(self, obj, path, theme):
        if isinstance(obj, BaseForm):
            return {'path': path.strip("/"),
                    'theme': theme,
                    'form': normalize(type(obj).__name__)}
        elif isinstance(obj, BaseFormSet):
            return {'path': path.strip("/"),
                    'theme': theme,
                    'formset': normalize(type(obj).__name__)}
        elif isinstance(obj, BoundField):
            return {'path': path.strip("/"),
                    'theme': theme,
                    'form': normalize(type(obj.form).__name__),
                    'field': normalize(obj.name),
                    'widget': normalize(type(obj.field.widget).__name__)}
        raise ValueError("Object {} of type {} is not supported by {}".format(obj, type(obj), type(self)))

    def get_template(self, obj, template_type, path=None, theme=None, patterns=None):
        path = path or Silhouette.PATH
        theme = theme or Silhouette.THEME
        patterns = patterns or Silhouette.PATTERNS
        substitutes = self.get_substitutes(obj, path, theme)
        templates = [pattern.format(**substitutes) for pattern in patterns[template_type]]
        return select_template(templates)

    def __call__(self, *args, **kwargs):
        return self.get_template(*args, **kwargs)


get_silhouette = loader = Silhouette.settings.LOADER()
