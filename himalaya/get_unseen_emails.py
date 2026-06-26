#!/usr/bin/env python3
import subprocess
import json

HIMALAYA_LIST = "/root/.hermes/scripts/himalaya/himalaya_list.sh"

result = subprocess.run(
    ["bash",HIMALAYA_LIST],
    capture_output=True,
    text=True,
    check=True)

emails = json.loads(result.stdout)

for e in emails:
    if "Seen" not in e['flags']:
        print(f"✉️ [{e['id']}] : {e['subject']}\nFrom : {e['from']['addr']} \n Date : {e['date']} \n")
