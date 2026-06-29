---
name: notion-event-adder
description: Add events to Notion database using event_details.json and notion_add.py.
---

# notion-event-adder

Workflow to add events to Notion:

1.  **Extract Details**: Write event information into `/root/.hermes/scripts/notion/event_details.json` using the required keys: 
    - `title`, `startDate`, `startTime`, `endDate`, `endTime`, `location`, `priority`, `tag`, `status`.
    - Fields can be left empty; defaults are handled by the script.
    - __Valid Tags__: "Life, Events, Career, Personal Project, Organization, Competition, School, Other".
    - __Valid Priorities__: "Low, Medium, High, CRITICAL".
    - __Valid Statuses__: "Not started, In progress, Done".

2.  **Execute Script**: Run the sync script:
    `python3 /root/.hermes/scripts/notion/notion_add.py`

3.  **Confirm**: After the script finishes, provide the user with the event details summary and the URL of the created Notion page.
