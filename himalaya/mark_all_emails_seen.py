#!/usr/bin/env python3
import subprocess
import json

HIMALAYA_LIST = "/root/.hermes/scripts/himalaya/himalaya_list.sh"
HIMALAYA_MARK_SEEN = "/root/.hermes/scripts/himalaya/himalaya_mark_seen.sh"

result = subprocess.run(
    ["bash",HIMALAYA_LIST],
    capture_output=True,
    text=True,
    check=True)

emails = json.loads(result.stdout)

for e in emails:
    subprocess.run(
        ["bash", HIMALAYA_MARK_SEEN, e['id']])
