import logging

from django.core.exceptions import ObjectDoesNotExist
from lms.djangoapps.utils import _get_key
from opaque_keys.edx.keys import CourseKey

from .models import GeneratedCertificate

log = logging.getLogger(__name__)


class CertificateService(object):
    """
    User Certificate service
    """

    def invalidate_certificate(self, user_id, course_key_or_id):
        """
        Get the generated certificate for user and invalidate its certificate when dropped below passing
        threshold due to suspicious proctored exam

        If generated certificate does not exist, do Nothing.
        """
        course_key = _get_key(course_key_or_id, CourseKey)
        try:
            generated_certificate = GeneratedCertificate.objects.get(  # pylint: disable=no-member
                user=user_id,
                course_id=course_key
            )
            generated_certificate.invalidate()
            log.info(
                u'Certificate invalidated for user %d in course %s when dropped below passing threshold due to '
                u'suspicious proctored exam',
                user_id,
                course_key
            )
        except ObjectDoesNotExist:
            pass
