"""
Overrides the default ratelimitbackend to use the AllowAllUsersModelBackend to preserve pre-1.10 Django functionality
in regards to authenticating users who are inactive.
"""

from ratelimitbackend.backends import RateLimitMixin

# TODO: Remove Django 1.11 upgrade shim
# SHIM: Post-upgrade we should only need the AllowAllUsersModelBackend.
try:
    from django.contrib.auth.backends import AllowAllUsersModelBackend as django_backend
except ImportError:
    from django.contrib.auth.backends import ModelBackend as django_backend


class RateLimitedAllUserBackend(RateLimitMixin, django_backend):
    """
    Just applies the mixin to the standard Django model backend for the version we're using
    """
    pass
