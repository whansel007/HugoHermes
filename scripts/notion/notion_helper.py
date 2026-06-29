import os
import json
import requests

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_VERSION = "2025-09-03"
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def search_page(page_name):
    url = "https://api.notion.com/v1/search"
    response = requests.post(url, headers=HEADERS, json={"query": page_name})
    results = response.json().get("results", [])
    if results:
        return results[0]["id"]
    return None

def create_page(parent_page_id, title, content_markdown):
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": [{"text": {"content": title}}]
        },
        "markdown": content_markdown
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()

def update_page_content(page_id, markdown_content):
    url = f"https://api.notion.com/v1/pages/{page_id}/markdown"
    payload = {"markdown": markdown_content}
    response = requests.patch(url, headers=HEADERS, json=payload)
    return response.json()

if __name__ == "__main__":
    # Example usage:
    # page_id = search_page("My Target Page")
    # if page_id:
    #     update_page_content(page_id, "## Updated via Python\nThis was added by a script.")
    print("Notion scripts ready. Import these functions to interact with Notion.")
