import json
import os
from datetime import datetime

# Paths
MUNITIONS_PATH = 'public/data/munitions-ledger.json'
CASUALTY_PATH = 'public/data/casualty-ledger.json'

# --- YOUR DATA INPUT ---
# Add new verified data here when you have it.
NEW_MUNITIONS = [
    # { "date": "2026-08-01", "description": "New Surge Event", "incurredCost": 5000000 }
]

NEW_CASUALTIES = [
    # { "date": "2026-08-01", "description": "New Event", "confirmedCasualties": 5 }
]

def update_json_ledger(file_path, new_entries, key_name):
    if not os.path.exists(file_path):
        data = []
    else:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
    if new_entries:
        data.extend(new_entries)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Successfully injected {len(new_entries)} entries into {key_name}.")
    else:
        print(f"No new entries for {key_name}.")

# Run updates
update_json_ledger(MUNITIONS_PATH, NEW_MUNITIONS, "Munitions Ledger")
update_json_ledger(CASUALTY_PATH, NEW_CASUALTIES, "Casualty Ledger")
