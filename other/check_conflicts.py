import requests
import os
import json

page_id = "1d2960a2ed918096a55adb7e776bf8e9"
api_token = os.environ.get("NOTION_API_KEY")

data = {
    "filter": {
        "and": [
            {
                "property": "Date",
                "date": {
                    "on_or_after": "2026-06-21T00:00:00+08:00"
                }
            },
            {
                "property": "Date",
                "date": {
                    "on_or_before": "2026-06-21T23:59:59+08:00"
                }
            }
        ]
    }
}

headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.post(f"https://api.notion.com/v1/databases/{page_id}/query", headers=headers, json=data)
print(json.dumps(response.json(), indent=2))
