import subprocess
import json
import os

page_id = "386960a2-ed91-8161-880f-cbda7d43196c"
api_token = os.environ.get("NOTION_API_KEY")

data = {
    "properties": {
        "Status": {
            "status": {
                "name": "Not started"
            }
        },
        "Date": {
            "date": {
                "start": "2026-06-21T20:00:00",
                "end": "2026-06-21T22:00:00"
            }
        }
    }
}

cmd = [
    "curl", "-s", "-X", "PATCH",
    f"https://api.notion.com/v1/pages/{page_id}",
    "-H", f"Authorization: Bearer {api_token}",
    "-H", "Notion-Version: 2022-06-28",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(data)
]

result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)

