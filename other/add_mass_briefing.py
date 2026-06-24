import requests
import os
import json

page_id = "1d2960a2ed918096a55adb7e776bf8e9"
api_token = os.environ.get("NOTION_API_KEY")

data = {
    "parent": { "database_id": page_id },
    "properties": {
        "Name": {
            "title": [{ "text": { "content": "Face-to-Face Mass Briefing" } }]
        },
        "Date": {
            "date": {
                "start": "2026-06-30T15:00:00+08:00",
                "end": "2026-06-30T17:00:00+08:00"
            }
        },
        "Tags": {
            "select": {
                "name": "Organization"
            }
        },
        "Location": {
            "rich_text": [
                {
                    "text": {
                        "content": "TBA"
                    }
                }
            ]
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
