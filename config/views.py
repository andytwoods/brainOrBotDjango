from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_auth.views import LogoutView


class TestAuthView(APIView):

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))
