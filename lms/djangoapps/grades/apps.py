"""
Grades Application Configuration

Signal handlers are connected here.
"""

from django.apps import AppConfig
from django.conf import settings
from edx_proctoring.runtime import set_runtime_service
from openedx.core.djangolib.django_plugins import ProjectType, SettingsType, PluginURLs, PluginSettings


class GradesConfig(AppConfig):
    """
    Application Configuration for Grades.
    """
    name = u'lms.djangoapps.grades'

    plugin_app = {
        PluginURLs.config: {
            ProjectType.lms: {
                PluginURLs.namespace: u'grades_api',
                PluginURLs.regex: u'api/grades/',
                PluginURLs.relative_path: u'api.urls',
            }
        },
        PluginSettings.config: {
            ProjectType.lms: {
                SettingsType.aws: {PluginSettings.relative_path: u'settings.aws'},
                SettingsType.common: {PluginSettings.relative_path: u'settings.common'},
                SettingsType.test: {PluginSettings.relative_path: u'settings.test'},
            }
        }
    }

    def ready(self):
        """
        Connect handlers to recalculate grades.
        """
        # Can't import models at module level in AppConfigs, and models get
        # included from the signal handlers
        from .signals import handlers  # pylint: disable=unused-variable
        if settings.FEATURES.get('ENABLE_SPECIAL_EXAMS'):
            from .services import GradesService
            set_runtime_service('grades', GradesService())
