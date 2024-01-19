import logging

logger = logging.getLogger("http-config")

class DVStreamHandler(logging.StreamHandler):
    def handle(self, record):
        msg = record.getMessage()
        if "/liveness" in msg:
            pass
        elif "/readiness" in msg:
            pass
        else:
            super().handle(record)