from dataclasses import dataclass
from datetime import datetime


@dataclass
class Measurement:
    time: datetime
    target: str
    metric: str
    value: float
