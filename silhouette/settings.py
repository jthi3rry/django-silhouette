LOADER = "silhouette.loaders.DefaultLoader"

THEME = "base"

PATTERNS = {
    'form': (
        "silhouette/{form}.html",
        "silhouette/{form}/form.html",
        "silhouette/{theme}/forms/form.html",
    ),
    'form_errors': (
        "silhouette/{form}/errors.html",
        "silhouette/{theme}/forms/errors.html",
    ),
    'form_fields': (
        "silhouette/{form}/fields.html",
        "silhouette/{theme}/forms/fields.html",
    ),
    'form_controls': (
        "silhouette/{form}/controls.html",
        "silhouette/{theme}/forms/controls.html",
    ),
    'form_media': (
        "silhouette/{form}/media.html",
        "silhouette/{theme}/forms/media.html",
    ),
    'formset': (
        "silhouette/{form}/formset.html",
        "silhouette/{theme}/formsets/formset.html",
    ),
    'field': (
        "silhouette/{form}/fields/{field}.html",
        "silhouette/{form}/fields/{widget}_field.html",
        "silhouette/{theme}/fields/{widget}_field.html",
        "silhouette/{form}/fields/field.html",
        "silhouette/{theme}/fields/field.html",
    ),
    'field_widget': (
        "silhouette/{form}/widgets/{field}.html",
        "silhouette/{form}/widgets/{widget}.html",
        "silhouette/{theme}/widgets/{widget}.html",
    ),
    'field_label': (
        "silhouette/{form}/fields/{field}_label.html",
        "silhouette/{form}/fields/label.html",
        "silhouette/{theme}/fields/label.html",
    ),
    'field_errors': (
        "silhouette/{form}/fields/{field}_errors.html",
        "silhouette/{form}/fields/errors.html",
        "silhouette/{theme}/fields/errors.html",
    ),
    'field_help_text': (
        "silhouette/{form}/fields/{field}_help_text.html",
        "silhouette/{form}/fields/help_text.html",
        "silhouette/{theme}/fields/help_text.html",
    ),
}
