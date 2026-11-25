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
