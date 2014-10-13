from django.template import Library
from django.forms import widgets
from django.forms.extras import widgets as extra_widgets
from django.utils.html import escape
from django.utils.safestring import mark_safe


register = Library()


@register.filter
def to_html_attrs(attrs):
    return mark_safe("".join([" {}=\"{}\"".format(attr, escape(val)) for attr, val in attrs.items()]))


@register.filter
def is_text_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.TextInput)


@register.filter
def is_number_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.NumberInput)


@register.filter
def is_email_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.EmailInput)


@register.filter
def is_date_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.DateInput)


@register.filter
def is_datetime_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.DateTimeInput)


@register.filter
def is_split_datetime_widget(bound_field):
    return isinstance(bound_field.field.widget, widgets.SplitDateTimeWidget)


@register.filter
def is_time_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.TimeInput)


@register.filter
def is_url_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.URLInput)


@register.filter
def is_password_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.PasswordInput)


@register.filter
def is_hidden_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.HiddenInput)


@register.filter
def is_multiple_hidden_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.MultipleHiddenInput)


@register.filter
def is_file_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.FileInput)


@register.filter
def is_clearable_file_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.ClearableFileInput)


@register.filter
def is_textarea(bound_field):
    return isinstance(bound_field.field.widget, widgets.Textarea)


@register.filter
def is_checkbox_input(bound_field):
    return isinstance(bound_field.field.widget, widgets.CheckboxInput)


@register.filter
def is_select(bound_field):
    return isinstance(bound_field.field.widget, widgets.Select)


@register.filter
def is_select_multiple(bound_field):
    return isinstance(bound_field.field.widget, widgets.SelectMultiple)


@register.filter
def is_radio_select(bound_field):
    return isinstance(bound_field.field.widget, widgets.RadioSelect)


@register.filter
def is_checkbox_select_multiple(bound_field):
    return isinstance(bound_field.field.widget, widgets.CheckboxSelectMultiple)


@register.filter
def is_null_boolean_select(bound_field):
    return isinstance(bound_field.field.widget, widgets.NullBooleanSelect)


@register.filter
def is_select_date_widget(bound_field):
    return isinstance(bound_field.field.widget, extra_widgets.SelectDateWidget)
