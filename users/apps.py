from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
# Override this method in subclasses to run code when Django starts.
    def ready(self):
        import users.signals
