from django.apps import AppConfig
from .singleton import get_global_object
import os

class Fs_viewerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fs_viewer'

    def ready(self):
        # Instantiate the global object when the app is ready
        # The check os.environ.get('RUN_MAIN') is a common way to prevent
        # the code from running twice in the development server's reloader.
        # In production WSGI servers, this check might not be necessary
        # or behave differently depending on the server.
        if os.environ.get('RUN_MAIN') or not os.environ.get('DJANGO_SETTINGS_MODULE'):
             # Avoid running during management commands where it's not needed
             # or in the separate process of the auto-reloader
             if not any(arg.startswith('manage.') for arg in os.sys.argv):
                 get_global_object()
                 print("Global object instantiated successfully in ready().")

