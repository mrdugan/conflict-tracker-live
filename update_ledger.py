import json
import os
from datetime import datetime

# Define the new event you want to inject
new_event = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "description": "Automated Logistics Attrition Update",
    "incurredCost": 12500000 
}

file_path = 'public/data/munitions-ledger.json'

# Load existing data
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = []

# Append and Save
data.append(new_event)
with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)
