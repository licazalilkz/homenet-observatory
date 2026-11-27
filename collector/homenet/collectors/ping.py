import subprocess
from datetime import datetime, timezone

from homenet.collectors.base import Collector
from homenet.models import Measurement


def parse_ping_output(output: str) -> dict[str, float]:
    resultado = {}
    for line in output.splitlines():
        if "packet loss" in line:
            loss = line.split(",")[2].split(" ")[1]
            resultado["packet_loss_pct"] = float(loss.replace("%", ""))
        if line.startswith("rtt"):
            avg = line.split("=")[1].split("/")[1]
            resultado["latency_ms"] = float(avg)
    return resultado


class PingCollector(Collector):
    name = "ping"

    def __init__(self, target: str):
        self.target = target

    def collect(self) -> list[Measurement]:
        saida = subprocess.run(
            ["ping", "-c", "4", self.target],
            capture_output=True,
            text=True,
        ).stdout
        metricas = parse_ping_output(saida)
        agora = datetime.now(timezone.utc)
        medicoes = []
        for nome, valor in metricas.items():
            medicao = Measurement(
                time=agora, target=self.target, metric=nome, value=valor
            )
            medicoes.append(medicao)
        return medicoes
