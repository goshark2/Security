import subprocess
import datetime

def get_event_logs():
    """Fetch event logs for changes in Event Manager in the last 24 hours."""
    time_filter = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
    
    command = f"powershell Get-WinEvent -LogName Security -MaxEvents 1000 | Where-Object {{$_.TimeCreated -ge '{time_filter}'}}"
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.stdout:
            print("[+] Event Manager Changes in Last 24 Hours:")
            print(result.stdout)
        else:
            print("[-] No changes detected in the last 24 hours.")
    except Exception as e:
        print(f"[!] Error fetching event logs: {e}")

if __name__ == "__main__":
    get_event_logs()
