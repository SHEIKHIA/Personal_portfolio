from django.apps import AppConfig

# Quote generator app is modeled in this class.
class QuoteGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quote_generator'
