
import subprocess
result = subprocess.run(['df', '/'], capture_output=True, text=True)


lines = result.stdout.strip().split('\n')
data = lines[1].split()


usage = data[4].replace('%', '')
print("Disk usage is:", usage)

threshold = 85
if int(usage) >= threshold:
    print("ALERT! Disk usage is above threshold!")
else:
    print("Disk usage is normal.")