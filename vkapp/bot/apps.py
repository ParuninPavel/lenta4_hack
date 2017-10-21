from django.apps import AppConfig


class BotConfig(AppConfig):
    name = 'vkapp.bot'
    verbose_name = "Bot"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
