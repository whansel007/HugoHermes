#!/usr/bin/env python3
print("Running...")

import subprocess
import json

HIMALAYA_LIST = "/root/.hermes/scripts/HugoHermes/himalaya_list.sh"

result = subprocess.run(
    ["bash",HIMALAYA_LIST],
    capture_output=True,
    text=True,
    check=True)

print(f"{result.stdout}")
emails = json.load(result.stdout)
print(f"Yo this is the email results : \n {emails}")
