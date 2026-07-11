#!/usr/bin/env python3
from google_api import get_service
from datetime import datetime, timedelta

def list_events(max_results=10, time_min=None, time_max=None):
    service = get_service()
    
    now_raw = datetime.now() 
    now = now_raw.strftime('%Y-%m-%dT%H:%M:%S+08:00')
    
    if time_max:
        response = service.events().list(
            calendarId="primary",
            maxResults=max_results,
            singleEvents=True,
            orderBy="startTime",
            timeMin=time_min or now,
            timeMax=time_max,
        ).execute()
    else:
        response = service.events().list(
            calendarId="primary",
            maxResults=max_results,
            singleEvents=True,
            orderBy="startTime",
            timeMin=time_min or now,
        ).execute()
    
    events = response.get("items", [])
    
    for e in events:
        title = e.get("summary", "(u forgot to title this one >_>)")
        start = e["start"].get("dateTime", e["start"].get("date"))
        print(f"{start} - {title}")
    
    return events
        
list_events()