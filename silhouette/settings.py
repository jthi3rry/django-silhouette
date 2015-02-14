LOADER = "silhouette.loaders.DefaultLoader"

PATH = "silhouette"

THEME = "default"

PATTERNS = {
    'form': (
        "{path}/{form}.html",
        "{path}/{form}/form.html",
        "{path}/{theme}/forms/form.html",
        "silhouette/base/forms/form.html",
    ),
    'form_errors': (
        "{path}/{form}/errors.html",
        "{path}/{theme}/forms/errors.html",
        "silhouette/base/forms/errors.html",
    ),
    'form_fields': (
        "{path}/{form}/fields.html",
        "{path}/{theme}/forms/fields.html",
        "silhouette/base/forms/fields.html",
    ),
    'form_controls': (
        "{path}/{form}/controls.html",
        "{path}/{theme}/forms/controls.html",
        "silhouette/base/forms/controls.html",
    ),
    'form_media': (
        "{path}/{form}/media.html",
        "{path}/{theme}/forms/media.html",
        "silhouette/base/forms/media.html",
    ),
    'formset': (
        "{path}/{formset}/formset.html",
        "{path}/{theme}/formsets/formset.html",
        "silhouette/base/formsets/formset.html",
    ),
    'formset_errors': (
        "{path}/{formset}/errors.html",
        "{path}/{theme}/formsets/errors.html",
        "silhouette/base/formsets/errors.html",
    ),
    'field': (
        "{path}/{form}/fields/{field}.html",
        "{path}/{form}/fields/{widget}_field.html",
        "{path}/{theme}/fields/{widget}_field.html",
        "{path}/{form}/fields/field.html",
        "{path}/{theme}/fields/field.html",
        "silhouette/base/fields/field.html",
    ),
    'field_label': (
        "{path}/{form}/fields/{field}_label.html",
        "{path}/{form}/fields/{widget}_label.html",
        "{path}/{theme}/fields/{widget}_label.html",
        "{path}/{form}/fields/label.html",
        "{path}/{theme}/fields/label.html",
        "silhouette/base/fields/label.html",
    ),
    'field_errors': (
        "{path}/{form}/fields/{field}_errors.html",
        "{path}/{form}/fields/{widget}_errors.html",
        "{path}/{theme}/fields/{widget}_errors.html",
        "{path}/{form}/fields/errors.html",
        "{path}/{theme}/fields/errors.html",
        "silhouette/base/fields/errors.html",
    ),
    'field_help_text': (
        "{path}/{form}/fields/{field}_help_text.html",
        "{path}/{form}/fields/{widget}_help_text.html",
        "{path}/{theme}/fields/{widget}_help_text.html",
        "{path}/{form}/fields/help_text.html",
        "{path}/{theme}/fields/help_text.html",
        "silhouette/base/fields/help_text.html",
    ),
    'field_widget': (
        "{path}/{form}/widgets/{field}.html",
        "{path}/{form}/widgets/{widget}.html",
        "{path}/{theme}/widgets/{widget}.html",
        # Silhouette renders the default widget when no templates are found, and therefore does not provide a base template
    ),
}
