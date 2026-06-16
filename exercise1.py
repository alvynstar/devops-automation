

threshold = 85
current_usage = 92
# check if current usage is above threshold
if current_usage >= threshold:
    print("ALERT! Disk usage is above threshold!")
else:
    print("Disk usage is normal")

threshold = 85

import subprocess
result = subprocess.run(['df', '/'], capture_output=True, text=True)
print(result.stdout)

# we'll extract the number next