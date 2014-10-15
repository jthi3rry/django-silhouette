Silhouette
==========

.. image:: https://travis-ci.org/OohlaLabs/django-silhouette.svg?branch=master
    :target: https://travis-ci.org/OohlaLabs/django-silhouette

.. image:: https://coveralls.io/repos/OohlaLabs/django-silhouette/badge.png?branch=master
    :target: https://coveralls.io/r/OohlaLabs/django-silhouette

.. attention::
   Work in progress

## Install

```python
# Not on pypi yet, but when it is :P
pip install silhouette
```


```python
INSTALLED_APPS += ['silhouette']

```


```python

SILHOUETTE = {
    'THEME': 'mytheme'
}

```

Create template folders

templates/silhouette
templates/silhouette/mytheme
templates/silhouette/mytheme/fields
templates/silhouette/mytheme/widgets

## Template Usage

### Render the form

``` html

{% load silhouette_tags %}

{% silhouette form %}

```

### Render a field

``` html

{% load silhouette_tags %}

{% field form.my_field widget_class="my_class" label_class="My Label" %}

```

## Theme Usage


### Overide all fields

templates/silhouette/my_theme/fields/field.html

``` html

{% extends "silhouette/base/fields/field.html" %}

{% load silhouette_tags silhouette_filters %}

{#{% block field %}#}
{#    <div class="row">#}
{#        {{ block.super }}#}
{#    </div>#}
{#{% endblock %}#}

{% block widget %}
    {% field_widget field class="form-control" %}
{% endblock %}


```

### Overide per form

templates/silhouette/mytheme/my_form.html

``` html

{% extends "silhouette/base/forms/form.html" %}

{% load silhouette_tags silhouette_filters %}


```


