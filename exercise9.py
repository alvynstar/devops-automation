import json

# Create a dictionary (Python's version of JSON)
server_data = {
    "server": "web-server-01",
    "disk_usage": 22,
    "cpu_usage": 15,
    "memory_usage": 45,
    "status": "healthy"
}

# Write to JSON file
with open('server_status.json', 'w') as file:
    json.dump(server_data, file, indent=2)

# Read from JSON file
with open('server_status.json', 'r') as file:
    data = json.load(file)
    print("Server:", data["server"])
    print("Disk Usage:", data["disk_usage"])
    print("Status:", data["status"])
