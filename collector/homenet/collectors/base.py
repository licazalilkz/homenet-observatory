from abc import ABC, abstractmethod
from homenet.models import Measurement


class Collector(ABC):
    name: str

    @abstractmethod
    def collect(self) -> list[Measurement]: ...
