import json
import requests
import os
from datetime import datetime, timedelta

# Constants
DATABASE_ID = "1d2960a2ed918096a55adb7e776bf8e9"
api_token = os.environ.get("NOTION_API_KEY")
now = datetime.now() 

# Get the AI written JSON file
event_details = {
  "title": "",
  "startDate": "",
  "startTime": "",
  "endDate":"",
  "endTime": "",
  "location": "",
  "priority":"",
  "tag": "",
  "status":""
}

try:
    with open("./scripts/notion/event_details.json") as f:
        event_details = json.load(f)
        print(event_details)
except Exception as e:
    print(e)

# Default Values if the AI didn't write anything
title = event_details['title'] or "Untitled Event"

startDate = event_details['startDate'] or now.strftime('%Y-%m-%d')
startTime = event_details['startTime'] or now.strftime('%H:%M')

endDate = event_details['endDate'] or (now + timedelta(hours=1)).strftime('%Y-%m-%d')
endTime = event_details['endTime'] or (now + timedelta(hours=1)).strftime('%H:%M')

location = event_details['location'] or "The Void"
priority = event_details['priority'] or "Medium"
tag = event_details['tag'] or "Life"

status = event_details['status'] or "Not started"

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
    }
}

headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
print(response.json())   