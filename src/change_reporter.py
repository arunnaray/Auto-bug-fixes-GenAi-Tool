import pandas as pd

def generate_report(changes: dict):
    data = []
    for module, msgs in changes.items():
        for msg in msgs:
            data.append({"Module": module, "Commit Message": msg, "Action": "Review Required"})
    return pd.DataFrame(data)
