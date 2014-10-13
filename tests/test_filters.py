import unittest

from collections import OrderedDict
from silhouette.templatetags import silhouette_filters
from tests.mock.forms import MockForm


class TestWidgetFilters(unittest.TestCase):

    def setUp(self):
        self.form = MockForm()

    def tearDown(self):
        self.form = None

    def assertAllTrue(self, list, func):
        if not all(func(item) for item in list):
            raise self.failureException("Some items weren't True: {}".format(filter(lambda item: not func(item), list)))

    def assertAllFalse(self, list, func):
        try:
            self.assertAllTrue(list, lambda item: not func(item))
        except self.failureException:
            raise self.failureException("Some items weren't False: {}".format(filter(func, list)))

    def assertWidgetFilterTruth(self, filter, fields):
        test_func = lambda field: filter(self.form[field])
        self.assertAllTrue(fields, test_func)
        self.assertAllFalse(set(self.form.fields) - set(fields), test_func)

    def test_is_text_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_text_input, {'text_input', 'email_input', 'url_input', 'number_input', 'password_input', 'date_input', 'datetime_input', 'time_input'})

    def test_is_number_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_number_input, {'number_input'})

    def test_is_email_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_email_input, {'email_input'})

    def test_is_url_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_url_input, {'url_input'})

    def test_is_password_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_password_input, {'password_input'})

    def test_is_hidden_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_hidden_input, {'hidden_input', 'multiple_hidden_input'})

    def test_is_multiple_hidden_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_multiple_hidden_input, {'multiple_hidden_input'})

    def test_is_file_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_file_input, {'file_input', 'clearable_file_input'})

    def test_is_clearable_file_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_clearable_file_input, {'clearable_file_input'})

    def test_is_date_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_date_input, {'date_input'})

    def test_is_datetime_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_datetime_input, {'datetime_input'})

    def test_is_time_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_time_input, {'time_input'})

    def test_is_split_datetime_widget(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_split_datetime_widget, {'split_datetime_widget'})

    def test_is_textarea(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_textarea, {'textarea'})

    def test_is_checkbox_input(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_checkbox_input, {'checkbox_input'})

    def test_is_select(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_select, {'select', 'null_boolean_select', 'radio_select', 'select_multiple', 'checkbox_select_multiple'})

    def test_is_select_multiple(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_select_multiple, {'select_multiple', 'checkbox_select_multiple'})

    def test_is_radio_select(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_radio_select, {'radio_select'})

    def test_is_checkbox_select_multiple(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_checkbox_select_multiple, {'checkbox_select_multiple'})

    def test_is_null_boolean_select(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_null_boolean_select, {'null_boolean_select'})

    def test_is_select_date_widget(self):
        self.assertWidgetFilterTruth(silhouette_filters.is_select_date_widget, {'select_date_widget'})


class TestFilters(unittest.TestCase):

    def test_to_html_attrs(self):
        self.assertEqual(' id="my-id" class="my-class my-other-class"', silhouette_filters.to_html_attrs(OrderedDict((('id', 'my-id'), ('class', 'my-class my-other-class')))))

