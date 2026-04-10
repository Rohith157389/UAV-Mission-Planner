import json
import os

HISTORY_FILE = "history.json"

def save_mission(mission_input, mission_output):
    history = show_history()
    history.append({
        "input": mission_input,
        "output": mission_output
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def show_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
