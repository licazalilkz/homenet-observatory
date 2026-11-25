from homenet.collectors.ping import parse_ping_output

PING_OK = """PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=8.92 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=8.70 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=9.96 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=116 time=9.08 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 8.695/9.164/9.962/0.480 ms"""

PING_NO_REPLY = """ PING 192.0.2.1 (192.0.2.1) 56(84) bytes of data.

--- 192.0.2.1 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3050ms """


def test_parse_ping_output_when_target_responds():
    assert parse_ping_output(PING_OK) == {"latency_ms": 9.164, "packet_loss_pct": 0.0}


def test_parse_ping_output_when_target_does_not_respond():
    assert parse_ping_output(PING_NO_REPLY) == {"packet_loss_pct": 100.0}
