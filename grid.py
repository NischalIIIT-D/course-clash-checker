import pandas as pd

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]


def fmt(minutes):
    return str(minutes // 60) + ":" + str(minutes % 60).zfill(2)


def build_grid(courses):
    rows = {}
    for t in range(510, 1200, 30):
        rows[fmt(t)] = {d: "" for d in DAYS}
    for c in courses:
        for m in c["meetings"]:
            for t in range(m["start"], m["end"], 30):
                label = fmt(t)
                if label in rows:
                    rows[label][m["day"]] = c["name"]
    return pd.DataFrame(rows).T