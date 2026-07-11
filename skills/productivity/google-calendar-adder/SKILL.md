---
name: google-calendar-adder
description: Add events to Google Calendar using event_details.json and calendar_create.py.
---

# google-calendar-adder

Workflow to add events to Google Calendar:

## 1. Prepare Event Details
Create or update `/root/.hermes/scripts/google/event_details.json` with the following structure:
```json
{
  "title": "Event Title",
  "startDate": "YYYY-MM-DD",
  "startTime": "HH:MM",
  "endDate": "YYYY-MM-DD", 
  "endTime": "HH:MM",
  "location": "Location Name",
  "description": "Event description"
}
```
All fields are optional - the script provides sensible defaults:
- Missing dates/times: Defaults to current time + 1 hour
- Missing title: "Untitled Event"
- Missing location: "The Void"
- Missing description: "Nuthin here ~"

## 2. Execute the Script
Run the calendar creation script:
```bash
python3 /root/.hermes/scripts/google/calendar_create.py
```

## 3. Confirm Creation
The script will output a link to the created Google Calendar event when successful.

## Notes
- Uses your existing Google Calendar credentials (`google_client_secret.json` and `google_token.json`)
- Events are added to your primary calendar
- Timezone is hardcoded to +08:00 (SGT) in the script
- Make sure your credential files are in `/root/.hermes/`

## Related Skills
- notion-event-adder: Similar workflow for Notion events
- google-workspace: General Google Workspace tools