import json
from StringIO import StringIO

import django
from django.core.management import call_command
from django.test import TestCase


class CommandsTestBase(TestCase):

    def _run_dummy_command(self, *args, **kwargs):
        """Runs the test command's execute method directly, and outputs a dict of the current context."""
        out = StringIO()
        call_command('tracked_dummy_command', *args, stdout=out, **kwargs)
        out.seek(0)
        return json.loads(out.read())

    def test_command(self):
        args = ['whee']
        kwargs = {'key1': 'default', 'key2': True}
        json_out = self._run_dummy_command(*args, **kwargs)
        self.assertEquals(json_out['command'].strip(), 'tracked_dummy_command')
