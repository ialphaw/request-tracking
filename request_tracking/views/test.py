from rest_framework.views import APIView
from rest_framework.response import Response

from request_tracking.mixins import Logging


class Test(Logging, APIView):
    def post(self, request):
        return Response("Hello World!")
