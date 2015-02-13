from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.formsets import formset_factory

class MockForm(forms.Form):

    text_input = forms.CharField(widget=forms.TextInput)
    email_input = forms.EmailField()
    url_input = forms.URLField()
    number_input = forms.IntegerField()
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_input = forms.BooleanField()
    hidden_input = forms.CharField(widget=forms.HiddenInput)
    multiple_hidden_input = forms.CharField(widget=forms.MultipleHiddenInput)
    file_input = forms.FileField(widget=forms.FileInput)
    clearable_file_input = forms.FileField()
    textarea = forms.CharField(widget=forms.Textarea)
    date_input = forms.DateField()
    datetime_input = forms.DateTimeField()
    time_input = forms.TimeField()
    split_datetime_widget = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    select = forms.ChoiceField((('option 1', 'Option 1'), ('option 2', 'Option 2')))
    null_boolean_select = forms.NullBooleanField()
    select_multiple = forms.ChoiceField((('option 1', 'Option 1'), ('option 2', 'Option 2')), widget=forms.SelectMultiple)
    checkbox_select_multiple = forms.ChoiceField((('option 1', 'Option 1'), ('option 2', 'Option 2')), widget=forms.CheckboxSelectMultiple)
    radio_select = forms.ChoiceField((('option 1', 'Option 1'), ('option 2', 'Option 2')), widget=forms.RadioSelect)
    select_date_widget = forms.DateField(widget=SelectDateWidget)


class MockForm2(forms.Form):
    field1 = forms.CharField(min_length=4, required=True)


MockFormSet = formset_factory(MockForm2, max_num=1, validate_max=True)
