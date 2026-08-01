import json
import os
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

MUNITIONS_PATH = 'public/data/munitions-ledger.json'
CASUALTY_PATH = 'public/data/casualty-ledger.json'

# --- 1. MANUAL INJECTIONS (For Munitions/Surges) ---
NEW_MUNITIONS = []
NEW_CASUALTIES = []

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
        print(f"No new manual entries for {key_name}.")

# --- 2. AUTOMATED DOD RSS SCRAPER (For Casualties) ---
def scrape_dod_casualties():
    print("Checking Defense.gov RSS for new casualty releases...")
    rss_url = "https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?max=10&ContentType=400&Site=945"
    
    try:
        req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        
        # Load existing ledger to prevent duplicates
        if os.path.exists(CASUALTY_PATH):
            with open(CASUALTY_PATH, 'r') as f:
                existing_data = json.load(f)
                existing_descriptions = [entry.get("description", "") for entry in existing_data]
        else:
            existing_data = []
            existing_descriptions = []

        new_findings = []
        
        # Parse the RSS feed items
        for item in root.findall('./channel/item'):
            title = item.find('title').text
            pub_date = item.find('pubDate').text
            
            # Look for trigger words in the press release title
            if "casualty" in title.lower() or "identifies" in title.lower():
                clean_date = datetime.strptime(pub_date[5:16], "%d %b %Y").strftime("%Y-%m-%d")
                
                # Check if we already logged this specific release
                if title not in existing_descriptions:
                    print(f"🚨 New DoD Casualty Release Found: {title}")
                    new_findings.append({
                        "date": clean_date,
                        "description": title,
                        "confirmedCasualties": 1, # Defaults to 1, you can manually adjust later if it's a mass casualty event
                        "automated_source": "DoD RSS"
                    })
        
        if new_findings:
            existing_data.extend(new_findings)
            with open(CASUALTY_PATH, 'w') as f:
                json.dump(existing_data, f, indent=2)
            print(f"Automated Scraper appended {len(new_findings)} new events to Casualty Ledger.")
        else:
            print("No new automated casualty events found today.")
            
    except Exception as e:
        print(f"Automated RSS Scrape Failed: {e}")

# --- 3. EXECUTE PIPELINE ---
update_json_ledger(MUNITIONS_PATH, NEW_MUNITIONS, "Munitions Ledger")
update_json_ledger(CASUALTY_PATH, NEW_CASUALTIES, "Casualty Manual Ledger")

# Run the automated scraper
scrape_dod_casualties()
