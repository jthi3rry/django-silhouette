def clear_app_settings_cache():
    # Clean up. Django Pods caches settings once loaded. Remove cached settings
    from silhouette.apps import Silhouette
    if hasattr(Silhouette.settings, 'PATH'):
        del Silhouette.settings.PATH
    if hasattr(Silhouette.settings, 'THEME'):
        del Silhouette.settings.THEME
    if hasattr(Silhouette.settings, 'PATTERNS'):
        del Silhouette.settings.PATTERNS
