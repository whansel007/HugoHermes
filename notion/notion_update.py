import requests
import os

page_id = "386960a2-ed91-81e9-80a1-f0fdd375a0fe"
api_token = os.environ.get("NOTION_API_KEY")

data = {
    "properties": {
        "Date": {
            "date": {
                "start": "2026-06-21T21:00:00+08:00",
                "end": "2026-06-21T21:30:00+08:00"
            }
        },
        "Priority": {
            "select": {
                "name": "Low"
            }
        },
        "Tags": {
            "select": {
                "name": "Life"
            }
        },
        "Location": {
            "rich_text": [
                {
                    "text": {
                        "content": "Bed"
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

response = requests.patch(f"https://api.notion.com/v1/pages/{page_id}", headers=headers, json=data)
print(response.json())
