import time
import requests
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
# Senstive Token data so paste your data below
TOKEN = "PASTE_YOUR_SPLUNK_TOKEN_HERE"

# We will watch the 'Public' folder
FOLDER_TO_WATCH = r"C:\Users\Public"
# ---------------------

def send_to_splunk(filepath, action):
    # Note: We use http (not https) because SSL is off
    url = "http://localhost:8088/services/collector/event"
    headers = {"Authorization": f"Splunk {TOKEN}"}
    
    payload = {
        "event": {
            "message": "Ransomware Simulation",
            "file": filepath,
            "action": action,
            "status": "Suspicious Activity"
        }
    }
    
    try:
        requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"SUCCESS: Sent alert to Splunk -> {action} on {filepath}")
    except Exception as e:
        print(f"Failed to send to Splunk: {e}")

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            send_to_splunk(event.src_path, "MODIFIED")
    
    def on_created(self, event):
        if not event.is_directory:
            send_to_splunk(event.src_path, "CREATED")

if __name__ == "__main__":
    print(f"--- AGENT RUNNING: Watching {FOLDER_TO_WATCH} ---")
    observer = Observer()
    observer.schedule(MyHandler(), FOLDER_TO_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()