import subprocess  # load subprocess library to run shell commands
import os  # load os library for file operations
from datetime import datetime  # load datetime to get current time

threshold = 85  # set the maximum acceptable disk usage percentage
log_file = "disk_monitor.log"  # set the filename where logs will be written

def check_disk(server):  # define a function that checks disk usage
    result = subprocess.run(['df', '/'], capture_output=True, text=True)  # run df command and capture the output
    lines = result.stdout.strip().split('\n')  # remove whitespace and split output by newline
    data = lines[1].split()  # get the second line and split it by spaces into a list
    usage = data[4].replace('%', '')  # get the 5th item (usage%) and remove the % symbol
    return usage  # send the usage number back to whoever called this function

servers = ["web-server-01", "db-server-01", "app-server-01"]  # list of servers to check

for server in servers:  # loop through each server in the list
    usage = check_disk(server)  # call the function and get the disk usage
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # get current time in YYYY-MM-DD HH:MM:SS format
    
    if int(usage) >= threshold:  # if disk usage is greater than or equal to threshold
        log_message = f"[{timestamp}] ALERT on {server}: Disk usage is {usage}%\n"  # create an alert message
    else:  # if disk usage is below threshold
        log_message = f"[{timestamp}] OK on {server}: Disk usage is {usage}%\n"  # create an OK message
    
    # write to log file
    with open(log_file, 'a') as file:  # open the log file in append mode (add without deleting old content)
        file.write(log_message)  # write the message to the file
    
    print(log_message.strip())  # print the message to the screen