from datetime import datetime, timezone
from homenet.models import Measurement


def test_measurement_time():
    time = datetime.now(timezone.utc)
    measurement = Measurement(
        time=time, target="8.8.8.8", metric="latency_ms", value=23.4
    )
    assert measurement.time == time


def test_measurement_target():
    measurement = Measurement(
        time=datetime.now(timezone.utc),
        target="8.8.8.8",
        metric="latency_ms",
        value=23.4,
    )
    assert measurement.target == "8.8.8.8"


def test_measurement_metric():
    measurement = Measurement(
        time=datetime.now(timezone.utc),
        target="8.8.8.8",
        metric="latency_ms",
        value=23.4,
    )
    assert measurement.metric == "latency_ms"


def test_measurement_value():
    measurement = Measurement(
        time=datetime.now(timezone.utc),
        target="8.8.8.8",
        metric="latency_ms",
        value=23.4,
    )
    assert measurement.value == 23.4
