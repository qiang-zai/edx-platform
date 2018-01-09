
from django.apps import AppConfig
from openedx.core.djangolib.django_plugins import ProjectType, PluginURLs


plugin_urls_config = {PluginURLs.namespace: u'theming', PluginURLs.regex: u'theming/'}


class ThemingConfig(AppConfig):
    name = 'openedx.core.djangoapps.theming'
    plugin_app = {
        PluginURLs.config: {
            ProjectType.cms: plugin_urls_config,
            ProjectType.lms: plugin_urls_config,
        }
    }
    verbose_name = "Theming"

    def ready(self):
        # settings validations related to theming.
        from . import checks
