#!/usr/bin/env python3
print("Running...")

import subprocess

HIMALAYA_LIST = "/root/himalaya_list.sh"

result = subprocess.run(
    ["bash",HIMALAYA_LIST],
    capture_output=True,
    text=True,
    check=True)

print(f"{result}")
