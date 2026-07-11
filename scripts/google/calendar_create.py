#!/usr/bin/env python3
from scripts.google.google_api import get_service
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
    
    endDate = raw.get('endDate') or (now + timedelta(hours=1)).strftime('%Y-%m-%d')
    endTime = raw.get('endTime') or (now + timedelta(hours=1)).strftime('%H:%M')
    
    location = raw.get('location') or "The Void"

    description = raw.get('description') or "Nuthin here ~"
    
    event = {
        "summary": summary,
        "start": {
            "dateTime": f"{startDate}T{startTime}:00+08:00"
            },
        "end":{
            "dateTime": f"{endDate}T{endTime}:00+08:00",
        },
        "location": location,
        "description": description,
    }
    
    result = service.events().insert(
        calendarId="primary",
        body=event).execute()
    
    print("Created: ", result.get("htmlLink"))

create_event()