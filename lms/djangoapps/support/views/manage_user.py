from django.utils.decorators import method_decorator
from django.views.generic import View
from edxmako.shortcuts import render_to_response
from lms.djangoapps.support.decorators import require_support_permission
from django.core.urlresolvers import reverse

from rest_framework.generics import GenericAPIView

from django.contrib.auth.models import User
from util.json_request import JsonResponse
from django.db.models import Q
from openedx.core.djangoapps.user_api.accounts.serializers import AccountUserSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model


class ManageUserSupportView(View):
    """
    View for viewing and managing user accounts, used by the
    support team.
    """

    @method_decorator(require_support_permission)
    def get(self, request):
        """Render the manage user support tool view."""
        return render_to_response('support/manage_user.html', {
            'username': request.GET.get('user', ''),
            'userSupportUrl': reverse('support:manage_user'),
            'userDetailUrl': reverse('support:manage_user_detail')
        })


class ManageUserDetailView(GenericAPIView):

    @method_decorator(require_support_permission)
    def get(self, request, username_or_email):

        try:
            user = get_user_model.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
            return Response(AccountUserSerializer(user, context={'request':request}).data)
        except User.DoesNotExist:
            return JsonResponse([])

    @method_decorator(require_support_permission)
    def post(self, request, username_or_email):
        """Allows support staff to disable a user's account."""
        user = get_user_model().objects.get(Q(username=username_or_email) | Q(email=username_or_email))
        user.set_unusable_password()
        user.save()
        return JsonResponse('User Disabled Successfully')
