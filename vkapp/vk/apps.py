from __future__ import unicode_literals

from django.apps import AppConfig


class VkConfig(AppConfig):
    name = 'vkapp.vk'
    verbose_name = "Vk"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
