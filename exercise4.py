import subprocess  # load the subprocess library so we can run shell commands

def check_disk(server):  # define a function called check_disk, it accepts one input called "server"
    result = subprocess.run(['df', '/'], capture_output=True, text=True)  # run "df /" command and store the output
    lines = result.stdout.strip().split('\n')  # remove whitespace and split output into lines
    data = lines[1].split()  # take the second line (actual data) and split by spaces into a list
    usage = data[4].replace('%', '')  # grab the 5th item (usage%) and remove the % sign
    return usage  # send the usage number back to whoever called this function

servers = ["web-server-01", "db-server-01", "app-server-01"]  # list of servers to check

for server in servers:  # loop through each server one by one
    usage = check_disk(server)  # call our function and store the result
    print("Disk usage on", server, "is", usage + "%")  # print the result