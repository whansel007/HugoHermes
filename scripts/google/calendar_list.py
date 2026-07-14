#!/usr/bin/env python3
from google_api import get_service
from datetime import datetime
import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set max Result amount, TimeMin, TimeMax")
    parser.add_argument("-r","--result", help="max Result amount", default=10)
    parser.add_argument("-min", "--timeMin", help="Minimum time for event", default=None)
    parser.add_argument("-max", "--timeMax", help="Maximum time for event", default=None)

    args = parser.parse_args()    
    list_events(
        max_results= args.result,
        time_min= args.timeMin,
        time_max=args.timeMax,
    )