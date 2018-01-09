"""
Configuration for the ace_common Django app.
"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from openedx.core.djangolib.django_plugins import ProjectType, PluginSettings, SettingsType


class AceCommonConfig(AppConfig):
    """
    Configuration class for the ace_common Django app.
    """
    name = 'openedx.core.djangoapps.ace_common'
    verbose_name = _('ACE Common')

    plugin_app = {
        PluginSettings.config: {
            ProjectType.lms: {
                SettingsType.aws: {PluginSettings.relative_path: u'settings.aws'},
                SettingsType.common: {PluginSettings.relative_path: u'settings.common'},
                SettingsType.devstack: {PluginSettings.relative_path: u'settings.common'},
            }
        }
    }
