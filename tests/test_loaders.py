import unittest
from django.forms.formsets import formset_factory
try:
    from django.template.backends.django import Template
except ImportError: #  pragma: nocover
    from django.template.base import Template
try:
    from django.template.base import TemplateDoesNotExist
except ImportError:
    from django.template.exceptions import TemplateDoesNotExist
from django.test.utils import override_settings

from .pods_utils import clear_app_settings_cache
from .mock import forms

from silhouette.loaders import loader


PATH = 'test_loaders'

THEME = 'loader'

PATTERNS = {
    "test_form": (
        "{path}/{theme}/{form}.html",
    ),
    "test_formset": (
        "{path}/{theme}/{formset}.html",
    ),
    "test_field": (
        "{path}/{theme}/{form}-{field}-{widget}.html",
    ),
    "test_fallback": (
        "{path}/{theme}/does-not-exist-1-{form}.html",
        "{path}/{theme}/does-not-exist-2-{form}.html",
        "{path}/{theme}/fallback-{form}.html",
    ),
    "test_notfound": (
        "{path}/{theme}/does-not-exist-1.html",
        "{path}/{theme}/does-not-exist-2.html",
    ),
}


class TestLoaders(unittest.TestCase):

    def tearDown(self):
        clear_app_settings_cache()

    def test_get_template_for_form(self):
        obj = forms.MockForm()
        self.assertIsInstance(loader.get_template(obj, 'test_form', path=PATH, theme=THEME, patterns=PATTERNS), Template)

    def test_get_template_for_formset(self):
        obj = formset_factory(forms.MockForm)()
        self.assertIsInstance(loader.get_template(obj, 'test_formset', path=PATH, theme=THEME, patterns=PATTERNS), Template)

    def test_get_template_for_field(self):
        obj = forms.MockForm()['text_input']
        self.assertIsInstance(loader.get_template(obj, 'test_field', path=PATH, theme=THEME, patterns=PATTERNS), Template)

    def test_get_template_using_fallback(self):
        obj = forms.MockForm()
        self.assertIsInstance(loader.get_template(obj, 'test_fallback', path=PATH, theme=THEME, patterns=PATTERNS), Template)

    def test_get_template_fail_when_not_found(self):
        obj = forms.MockForm()
        with self.assertRaises(TemplateDoesNotExist):
            loader.get_template(obj, 'test_notfound', path=PATH, theme=THEME, patterns=PATTERNS)

    def test_get_template_fail_when_object_not_supported(self):
        with self.assertRaises(ValueError):
            loader.get_template(object(), 'test_form', path=PATH, theme=THEME, patterns=PATTERNS)

    def test_loader_is_callable(self):
        obj = forms.MockForm()
        self.assertIsInstance(loader(obj, 'test_form', path=PATH, theme=THEME, patterns=PATTERNS), Template)

    @override_settings(SILHOUETTE_PATH=PATH, SILHOUETTE_THEME=THEME, SILHOUETTE_PATTERNS=PATTERNS)
    def test_get_template_with_user_settings_overrides(self):
        obj = forms.MockForm()
        self.assertIsInstance(loader.get_template(obj, 'test_form'), Template)
