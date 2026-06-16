import subprocess
import requests
import os

threshold = 20

def check_disk(server):
    result = subprocess.run(['df', '/'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    data = lines[1].split()
    usage = data[4].replace('%', '')
    return usage

servers = ["web-server-01", "db-server-01", "app-server-01"]

for server in servers:
    usage = check_disk(server)
    print("Disk usage on", server, "is", usage + "%")

    if int(usage) >= threshold:
        slack_webhook = os.environ.get("SLACK_WEBHOOK_URL")
        message = f"ALERT! Disk usage is {usage}% on {server}. Cleanup triggered."
        requests.post(slack_webhook, json={"text": message})
        print("Slack alert sent!")
        print("ALERT! Disk usage is above threshold on", server)
        cleanup = subprocess.run(
            ['find', '/var/log', '-type', 'f', '-mtime', '+30', '-delete'],
            capture_output=True, text=True
        )
        print("Log cleanup completed on", server)
    else:
        print("Disk usage is normal on", server)