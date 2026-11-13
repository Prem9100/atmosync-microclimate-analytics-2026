from src.atmosync.producer import delivery_report


class FakeMessage:
    def topic(self):
        return "atmosync.sensor.telemetry"

    def partition(self):
        return 0

    def offset(self):
        return 123


def test_delivery_report_success(caplog):
    with caplog.at_level("INFO"):
        delivery_report(None, FakeMessage())

    assert "Kafka delivered" in caplog.text
    assert "atmosync.sensor.telemetry" in caplog.text


def test_delivery_report_failure(caplog):
    with caplog.at_level("ERROR"):
        delivery_report(Exception("Kafka delivery failed"), None)

    assert "Delivery failed" in caplog.text
