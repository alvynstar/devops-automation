import subprocess
result = subprocess.run(['df', '/'], capture_output=True, text=True)
lines = result.stdout.strip().split('\n')
data = lines[1].split()
usage = data[4].replace('%', '')
# print("Disk usage is:", usage)

threshold = 85


servers = ["web-server-01", "db-server-01", "app-server-01"]
for server in servers:
    print("Checking server:", server)
    if int(usage) > threshold:
        print("Disk usage is high on", server)
    else:
        print("Disk usage is normal on", server)