#!/usr/bin/env python3
from scripts.google.google_api import get_service
from scripts.google.calendar_list import list_events
from datetime import datetime, timedelta
import json

EVENT_PATH = "/root/.hermes/scripts/google/event_details.json"
def create_event():
    service = get_service()
    
    now = datetime.now() 
    
    # Load in the raw AI written JSON file
    raw = {}
    try:
        with open(EVENT_PATH, "r") as f:
            raw = json.load(f)
    except Exception as e:
        print(e)
        
    # Input validation
    summary = raw.get('title') or "Untitled Event"
    
    startDate = raw.get('startDate') or now.strftime('%Y-%m-%d')
    startTime = raw.get('startTime') or now.strftime('%H:%M')
    startDateTime = f"{startDate}T{startTime}:00+08:00"
    
    endDate = raw.get('endDate') or (now + timedelta(hours=1)).strftime('%Y-%m-%d')
    endTime = raw.get('endTime') or (now + timedelta(hours=1)).strftime('%H:%M')
    endDateTime = f"{endDate}T{endTime}:00+08:00"
    
    location = raw.get('location') or "???"

    description = raw.get('description') or ""
    
    # Conflict Check
    conflicts = list_events(time_min=startDateTime, time_max=endDateTime)
    if not conflicts:
        print("No conflicts.")
    else:
        print(f"{len(conflicts)} conflict(s) detected!!!")
        print("The conflicting events are:")
        
        for e in conflicts:
            title = e.get("summary", "(u forgot to title this one >_>)")
            start = e["start"].get("dateTime", e["start"].get("date"))
            end = e["end"].get("dateTime", e["end"].get("date"))
            print(f"{start} - {end} : {title}")
        
        y_n = input("Create anyway? [Y/N] : ")
        while y_n not in ["Y", "N", "y", "n"]:
            print("Please only enter 'Y' or 'N'")
            y_n = input("Create anyway? [Y/N] : ")
        
        if y_n in ["N", "n"]:
            print("Event not created.")
            return
        
    # Event Creation
    event = {
        "summary": summary,
        "start": {
            "dateTime": startDateTime,
            },
        "end":{
            "dateTime": endDateTime,
        },
        "location": location,
        "description": description,
    }
    
    result = service.events().insert(
        calendarId="primary",
        body=event).execute()
    
    print("Created: ", result.get("htmlLink"))

create_event()