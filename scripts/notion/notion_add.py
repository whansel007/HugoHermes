import json
import requests
import os
from datetime import datetime, timedelta

# Constants
DATABASE_ID = "1d2960a2ed918096a55adb7e776bf8e9"
api_token = os.environ.get("NOTION_API_KEY")
now = datetime.now() 

# Get the AI written JSON file
try:
    with open("./scripts/notion/event_details.json") as f:
        event_details = json.load(f)
        print(event_details)
except Exception as e:
    print(e)
    event_details = {}

# Default Values if the AI didn't write anything
title = event_details.get('title') or "Untitled Event"
startDate = event_details.get('startDate') or now.strftime('%Y-%m-%d')
startTime = event_details.get('startTime') or now.strftime('%H:%M')
endDate = event_details.get('endDate') or (now + timedelta(hours=1)).strftime('%Y-%m-%d')
endTime = event_details.get('endTime') or (now + timedelta(hours=1)).strftime('%H:%M')
location = event_details.get('location') or "The Void"
priority = event_details.get('priority') or "Medium"
tag = event_details.get('tag') or "Life"
status = event_details.get('status') or "Not started"
markdown_content = event_details.get('markdown') or ""

# Filling in the data
data = {
    "parent": { "database_id": DATABASE_ID },
    "properties": {
        "Name": {
            "title": [{ "text": { "content": title } }]
        },
        "Date": {
            "date": {
                "start": f"{startDate}T{startTime}:00+08:00",
                "end": f"{endDate}T{endTime}:00+08:00"
            }
        },
        "Location": {
            "rich_text": [
                {
                    "text": {
                        "content": location
                    }
                }
            ]
        },
        "Priority": {
            "select": {
                "name": priority
            }
        },
        "Tags": {
            "select": {
                "name": tag
            }
        },
        "Status": {
            "status": { "name": status }
        },
    },
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": markdown_content}}]
            }
        }
    ]
}

headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=json.dumps(data))
print(response.json())
