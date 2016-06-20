from __future__ import unicode_literals

from django.test import SimpleTestCase
from django.template.context import Context
try:
    from django.template.base import TemplateDoesNotExist
except ImportError:
    from django.template.exceptions import TemplateDoesNotExist
try:
    from django.template.loader import get_template_from_string
except ImportError:
    from django.template import engines
    get_template_from_string = engines['django'].from_string

from django.test.utils import override_settings

from .pods_utils import clear_app_settings_cache

from .mock.forms import MockForm, MockFormSet
from .mock.tags import MockTag


@override_settings(SILHOUETTE_PATH="test_tags/base/silhouette",
                   SILHOUETTE_PATTERNS = {"mock_tag": ("{path}/{theme}/{form}.html",)})
class TestBaseTag(SimpleTestCase):

    def setUp(self):
        self.form = MockForm()
        self.context = Context({"myform": self.form})

    def tearDown(self):
        self.context = None
        clear_app_settings_cache()

    def test_template_type(self):
        tag = MockTag(self.context, self.form)
        self.assertEqual("mock_tag", tag.template_type)

    def test_template(self):
        tag = MockTag(self.context, self.form)
        self.assertEqual("silhouette/theme/mock_form", tag.render(self.context))

    def test_theme_override(self):
        tag = MockTag(self.context, self.form, theme="theme2")
        self.assertEqual("silhouette/theme2/mock_form", tag.render(self.context))

    def test_path_override(self):
        tag = MockTag(self.context, self.form, path="test_tags/base/silhouette2")
        self.assertEqual("silhouette2/theme/mock_form", tag.render(self.context))

    def test_template_override(self):
        tag = MockTag(self.context, self.form, template="test_tags/base/silhouette/mock_form.html")
        self.assertEqual("silhouette/mock_form", tag.render(self.context))

    def test_attributes(self):
        tag = MockTag(self.context, self.form, attr="attr")

        self.assertNotIn("obj", self.context)
        self.assertNotIn("attrs", self.context)

        with tag as local_context:
            self.assertEqual(self.context, local_context)
            self.assertDictContainsSubset({
                "obj": self.form,
                "attrs": {"attr": "attr"},
            }, self.context)

        self.assertNotIn("obj", self.context)
        self.assertNotIn("attrs", self.context)

    def test_cascaded_attributes(self):
        tag1 = MockTag(self.context, self.form, cascaded_attr1="cascaded", cascaded_attr2="cascaded")
        tag2 = MockTag(self.context, self.form, attr1="overriden")

        self.assertNotIn("cascaded_attrs", self.context)
        self.assertNotIn("attrs", self.context)

        with tag1 as outer_context:
            with tag2 as inner_context:
                self.assertEqual(inner_context, outer_context)
                self.assertDictContainsSubset({
                    "obj": self.form,
                    "attrs": {"attr1": "overriden", "attr2": "cascaded"},
                }, self.context)

        self.assertNotIn("cascaded_attrs", self.context)
        self.assertNotIn("attrs", self.context)

    def test_merge_cascaded_classes(self):
        tag1 = MockTag(self.context, self.form, cascaded_class="cascaded")
        tag2 = MockTag(self.context, self.form, **{"class": "non-cascaded"})

        with tag1:
            with tag2:
                self.assertIn("cascaded", self.context['attrs']['class'].split())
                self.assertIn("non-cascaded", self.context['attrs']['class'].split())

    def test_empty_prefixes(self):
        tag = MockTag(self.context, self.form)
        self.assertDictEqual({"attrs": {'attr': 'attr'}}, tag.build_attrs({'attr': 'attr'}))

    def test_tag(self):
        template_source = """{% load silhouette_tags %}{% mock myform class="form-class" %}"""
        template_target = """silhouette/theme/mock_form"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())


@override_settings(SILHOUETTE_PATH="test_tags/forms")
class TestFormTags(SimpleTestCase):

    def setUp(self):
        self.form = MockForm()
        self.context = Context({"form": self.form})

    def tearDown(self):
        self.form = None
        self.context = None
        clear_app_settings_cache()

    def test_form(self):
        template_source = """{% load silhouette_tags %}{% silhouette form action="/" %}"""
        template_target = """<form action="/"></form>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_form_media(self):
        template_source = """{% load silhouette_tags %}{% form_media form %}"""
        template_target = """<!-- media -->"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_form_media_missing_template(self):
        template_source = """{% load silhouette_tags %}{% form_media form template="does/not/exist.html" %}"""
        template_target = ""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_form_errors(self):
        template_source = """{% load silhouette_tags %}{% form_errors form id="form-errors" %}"""
        template_target = """<ul id="form-errors"></ul>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_form_errors_missing_template(self):
        template_source = """{% load silhouette_tags %}{% form_errors form id="form-errors" template="does/not/exist.html" %}"""
        template_target = ""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_form_fields(self):
        template_source = """{% load silhouette_tags %}{% form_fields form class="form-fields" %}"""
        template_target = """<div class="form-fields"><!-- field 1 here --></div><div class="form-fields"><!-- field 2 here --></div>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_form_fields_missing_template(self):
        template_source = """{% load silhouette_tags %}{% form_fields form class="form-fields" template="does/not/exist.html" %}"""
        with self.assertRaises(TemplateDoesNotExist):
            get_template_from_string(template_source).render(self.context)

    def test_form_controls(self):
        template_source = """{% load silhouette_tags %}{% form_controls form class="form-controls" %}"""
        template_target = """<button type="submit" class="form-controls">Submit</button>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_form_controls_missing_template(self):
        template_source = """{% load silhouette_tags %}{% form_controls form class="form-controls" template="does/not/exist.html" %}"""
        template_target = ""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())


@override_settings(SILHOUETTE_PATH="test_tags/formsets")
class TestFormsetTags(SimpleTestCase):

    def setUp(self):
        self.form = MockForm({})
        self.formset = MockFormSet(data={'form-TOTAL_FORMS': '2',
                                         'form-INITIAL_FORMS': '0',
                                         'form-MAX_NUM_FORMS': '',
                                         'form-0-field1': u'val',
                                         'form-1-field1': u'value',})
        self.context = Context({"form": self.form, 'formset': self.formset})

    def tearDown(self):
        self.form = None
        self.formset = None
        self.context = None
        clear_app_settings_cache()

    def test_formset(self):
        template_source = """{% load silhouette_tags %}{% formset formset %}"""
        result = get_template_from_string(template_source).render(self.context).strip()
        self.assertIn("""<ul><li>Please submit 1 or fewer forms.</li></ul>""", result)
        self.assertIn("""<input id="id_form-TOTAL_FORMS" name="form-TOTAL_FORMS" type="hidden" value="2" />""", result)
        self.assertIn("""<ul><li>Ensure this value has at least 4 characters (it has 3).</li></ul>""", result)
        self.assertIn("""<label for="id_form-1-field1">Field1:</label><input id="id_form-1-field1" name="form-1-field1" type="text" value="value" />""", result)

    def test_formset_errors(self):
        template_source = """{% load silhouette_tags %}{% formset_errors formset %}"""
        template_target = """<ul><li>Please submit 1 or fewer forms.</li></ul>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())


@override_settings(SILHOUETTE_PATH="test_tags/fields")
class TestFieldTags(SimpleTestCase):

    def setUp(self):
        self.form = MockForm({})
        self.context = Context({"form": self.form})

    def tearDown(self):
        self.form = None
        self.context = None
        clear_app_settings_cache()

    def test_field(self):
        template_source = """{% load silhouette_tags %}{% field form.url_input widget_class="url-widget" label_class="url-label" label_contents="I need a url" help_text_contents="Url should look like http://example.org" widget_id="widget-id" %}"""
        template_target = """<label class="url-label" for="widget-id">I need a url:</label><input class="url-widget" id="widget-id" name="url_input" type="url" /><p>Url should look like http://example.org</p><ul><li>This field is required.</li></ul>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_field_label(self):
        template_source = """{% load silhouette_tags %}{% field_label form.text_input class="label-class" id="label-id" contents="Aren't I awesome" suffix="?" %}"""
        template_target = """<label class="label-class" for="id_text_input" id="label-id">Aren't I awesome?</label>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_field_widget(self):
        template_source = """{% load silhouette_tags %}{% field_widget form.text_input class="field-class" id="field-id" %}"""
        template_target = """<input class="field-class" id="field-id" name="text_input" type="text" />"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_field_help_text(self):
        template_source = """{% load silhouette_tags %}{% field_help_text form.text_input class="field-help" contents="Need any help?" %}"""
        template_target = """<p class="field-help">Need any help?</p>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_field_help_text_missing_template(self):
        template_source = """{% load silhouette_tags %}{% field_help_text form.text_input template="does/not/exist.html" %}"""
        template_target = ""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_field_errors_text(self):
        template_source = """{% load silhouette_tags %}{% field_errors form.email_input class="field-errors" %}"""
        template_target = """<ul class="field-errors"><li>This field is required.</li></ul>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())

    def test_field_errors_missing_template(self):
        template_source = """{% load silhouette_tags %}{% field_errors form.email_input template="does/not/exist.html" %}"""
        template_target = """<ul class="errorlist"><li>This field is required.</li></ul>"""
        self.assertEqual(template_target, get_template_from_string(template_source).render(self.context).strip())
