import socket
import datetime
import pandas as pd

def add_log(agent_ip_address, port_number, community_string, action, value, out):
    # Get the hostname of the manager
    hostname = socket.gethostname()

    # Get the IP address of the manager
    manager_ip_address = socket.gethostbyname(hostname)
    
    # get current date and time
    time = datetime.datetime.now()
    import csv

    # open the CSV file in append mode
    with open('logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        row = [ time,agent_ip_address,manager_ip_address ,port_number,action,community_string, value, out]
        writer.writerow(row)