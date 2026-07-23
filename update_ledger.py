import json
import os
from datetime import datetime

# Path to your ledger
file_path = 'public/data/munitions-ledger.json'

# --- YOUR DATA INPUT ---
# Add your new verified events here when you have them.
# Even if you leave this empty, the script will run safely without errors.
new_events = [
    # {
    #     "date": "2026-07-23",
    #     "description": "Verified Attrition Event",
    #     "incurredCost": 5000000
    # }
]

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = []

# Only add if there is new data to inject
if new_events:
    data.extend(new_events)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Successfully injected {len(new_events)} new events.")
else:
    print("No new events to inject today.")
