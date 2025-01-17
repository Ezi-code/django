"""make toast test file."""

from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastTests(SimpleTestCase):
    """Test make_toast test case."""

    def test_make_toast(self):
        """Test make_toast function."""
        self.assertEqual(make_toast(), "toast")
