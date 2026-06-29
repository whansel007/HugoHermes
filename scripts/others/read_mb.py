import json
import subprocess

# List all emails to get IDs again if needed, or use the one we already have
with open("all_emails.json") as f:
    emails = json.load(f)

for e in emails:
    if "morning brew" in e["subject"].lower():
        print(f"--- Reading ID {e["id"]} ---")
        subprocess.run(["himalaya", "message", "read", str(e["id"])])
