import requests
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

headers = {
    "Authorization": f"Bearer {api_token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.patch(f"https://api.notion.com/v1/pages/{page_id}", headers=headers, json=data)
print(response.json())
