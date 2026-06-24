import requests
import os
import json

page_id = "386960a2-ed91-8198-835a-d2a838c7da75"
api_token = os.environ.get("NOTION_API_KEY")

# SGT is UTC+8. To set 18:30 SGT, we need to adjust the ISO string.
# 18:30 SGT = 10:30 UTC. 
# Notion API supports ISO 8601 with offset.
# Let's use 2026-06-21T18:30:00+08:00
data = {
    "properties": {
        "Date": {
            "date": {
                "start": "2026-06-21T18:30:00+08:00",
                "end": "2026-06-21T19:00:00+08:00"
            }
        }
    }
}

headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.patch(f"https://api.notion.com/v1/pages/{page_id}", headers=headers, json=data)
print(response.json())
