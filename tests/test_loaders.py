import unittest
from django.forms.formsets import formset_factory
from django.template.base import Template

from tests.mock import forms
from silhouette.loaders import loader


class TestLoaders(unittest.TestCase):

    def setUp(self):
        self.form = forms.MockForm()
        self.formset = formset_factory(forms.MockForm)()
        self.field = self.form['text_input']

    def test_get_substitutes_for_forms(self):
        self.assertDictEqual(loader.get_substitutes(self.form), {'theme': 'test', 'form': 'mock_form'})

    def test_get_substitutes_for_formset(self):
        self.assertDictEqual(loader.get_substitutes(self.formset), {'theme': 'test', 'formset': 'mock_form_form_set'})

    def test_get_substitutes_for_fields(self):
        self.assertDictEqual(loader.get_substitutes(self.field), {'theme': 'test', 'field': 'text_input', 'widget': 'text_input', 'form': 'mock_form'})

    def test_get_substitutes_for_unknowns(self):
        with self.assertRaises(ValueError):
            loader.get_substitutes(object())

    def test_get_template(self):
        self.assertIsInstance(loader.get_template('form_test', self.form), Template)

    def test_loader_is_callable(self):
        self.assertIsInstance(loader('form_test', self.form), Template)
