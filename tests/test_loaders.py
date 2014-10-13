import unittest
from django.template.base import Template

from tests.mock import forms
from silhouette.loaders import loader


class TestLoaders(unittest.TestCase):

    def setUp(self):
        self.form = forms.MockForm()

    def test_get_substitutes_for_forms(self):
        self.assertDictEqual(loader.get_substitutes(self.form), {'theme': 'test', 'form': 'mock_form'})

    def test_get_substitutes_for_fields(self):
        self.assertDictEqual(loader.get_substitutes(self.form['text_input']), {'field': 'text_input', 'theme': 'test', 'widget': 'text_input', 'form': 'mock_form'})

    def test_get_substitutes_for_unknowns(self):
        with self.assertRaises(ValueError):
            loader.get_substitutes(object())

    def test_get_template(self):
        self.assertIsInstance(loader.get_template('form_test', self.form), Template)

    def test_loader_is_callable(self):
        self.assertIsInstance(loader('form_test', self.form), Template)
