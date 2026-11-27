from homenet.models import Measurement
import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def connect():
    return psycopg.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        dbname=os.environ["DB_NAME"],
    )


def get_target_id(conn, name: str) -> int | None:
    row = conn.execute("SELECT id FROM targets WHERE name = %s", (name,)).fetchone()
    if row is None:
        return None
    return row[0]


def create_target(conn, name: str, host: str, kind: str) -> int:
    row = conn.execute(
        "INSERT INTO targets (name, host, kind) VALUES (%s, %s, %s) RETURNING id",
        (name, host, kind),
    ).fetchone()
    return row[0]


def save_measurements(conn, measurements: list[Measurement], kind: str) -> None:
    for m in measurements:
        target_id = get_target_id(conn, m.target)
        if target_id is None:
            target_id = create_target(conn, m.target, m.target, kind)
        conn.execute(
            "INSERT INTO measurements (time, target_id, metric, value) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
            (m.time, target_id, m.metric, m.value),
        )
    conn.commit()
