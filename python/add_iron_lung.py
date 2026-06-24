import requests
import os
import json

page_id = "1d2960a2ed918096a55adb7e776bf8e9"
api_token = os.environ.get("NOTION_API_KEY")

data = {
    "parent": { "database_id": page_id },
    "properties": {
        "Name": {
            "title": [{ "text": { "content": "Watch Iron Lung" } }]
        },
        "Date": {
            "date": {
                "start": "2026-06-21T18:00:00+08:00",
                "end": "2026-06-21T21:15:00+08:00"
            }
        },
        "Status": {
            "status": { "name": "Not started" }
        }
    }
}

headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
print(response.json())
