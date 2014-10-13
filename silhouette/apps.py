try:
    from django.apps import AppConfig
except:  # pragma: no cover
    class AppConfig(object):
        def __init__(self, *args, **kwargs):
            pass

from pods.apps import AppSettings


class Silhouette(AppSettings, AppConfig):
    name = "silhouette"
    settings_module = "silhouette.settings"
    settings_imports = ('LOADER',)
