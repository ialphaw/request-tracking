from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from request_tracking.mixins import Logging


class MockNoLoggingView(APIView):
    def get(self, request):
        return Response("no logging")


class MockLoggingView(Logging, APIView):
    def get(self, request):
        return Response("with logging")


class MockExplicitLoggingView(Logging, APIView):
    logging_methods = ["POST"]

    def get(self, request):
        return Response("no logging")

    def post(self, request):
        return Response("with logging")


class MockCustomCheckLoggingView(Logging, APIView):
    def should_log(self, request, response):
        return "log" in response.data

    def get(self, request):
        return Response("with logging")

    def post(self, request):
        return Response("no recording")


class MockSessionAuthLoggingView(Logging, APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("with session auth logging")


class MockSensitiveFieldsLoggingView(Logging, APIView):
    sensitive_fields = {"mY_fiEld"}

    def get(self, request):
        return Response("with logging")


class MockInvalidCleanedSubstituteLoggingView(Logging, APIView):
    CLEANED_SUBSTITUTE = 1
