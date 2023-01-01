from request_tracking.mixins import BaseLogging
from request_tracking.models import APIRequestLog


class Logging(BaseLogging):
    def handle_log(self):
        APIRequestLog(**self.log).save()
