import tkinter as tk
from SNMP import *
from logs import *
root = tk.Tk()
root.title("SNMP Tool")
root.geometry("470x300")

# IP Address
ip_label = tk.Label(root, text="IP Address:")
ip_label.grid(row=0, column=0, pady=5, padx = 10)
ip_entry = tk.Entry(root, width = 50)
ip_entry.grid(row=0, column=1)

# Port Number
port_label = tk.Label(root, text="Port Number:")
port_label.grid(row=1, column=0, pady=5, padx = 10)
port_entry = tk.Entry(root, width = 50)
port_entry.grid(row=1, column=1)

# Community String
comm_label = tk.Label(root, text="Community String:")
comm_label.grid(row=2, column=0, pady=5, padx = 10)
comm_entry = tk.Entry(root, width = 50)
comm_entry.grid(row=2, column=1)

# OID
oid_label = tk.Label(root, text="OID:")
oid_label.grid(row=3, column=0, pady=5, padx = 10)
oid_entry = tk.Entry(root, width = 50)
oid_entry.grid(row=3, column=1)

# Drop Down List
action_label = tk.Label(root, text="Action:")
action_label.grid(row=4, column=0, pady=5, padx = 10)
action_var = tk.StringVar(root)
action_var.set("GET")  # default value

def show_value_input(value):
    if value == "SET":
        value_label.grid(row=5, column=0, pady=5, padx = 10)
        value_entry.grid(row=5, column=1)
        submit_button.grid(row=6, column=1)
    else:
        value_label.grid_forget()
        value_entry.grid_forget()
        submit_button.grid(row=5, column=1)

action_option = tk.OptionMenu(root, action_var, "GET", "SET", "GETNEXT", command=show_value_input)
action_option.config(width=27)
action_option.grid(row=4, column=1, padx = 10)

# Value Input (Initially Hidden)
value_label = tk.Label(root, text="Value:")
value_entry = tk.Entry(root, width = 50)

# Submit Button
def submit():
    ip_address = ip_entry.get()
    port_number = port_entry.get()
    community_string = comm_entry.get()
    oid = oid_entry.get()
    action = action_var.get()
    value = value_entry.get() if action == "SET" else None
    if (ip_address == "" or community_string == "" or port_number == "" or oid == "" or (value == "" and action == "SET")):
        out = "please enter all the required inputs"
    else:
        if action == "SET":
            out = SET(ip_address, community_string, port_number, oid, value)
        if action == "GET":
            out = GET(ip_address, community_string, port_number, oid)
        if action == "GETNEXT":
            out = GETNEXT(ip_address, community_string, port_number, oid)
        add_log(ip_address, port_number, community_string, action, value, out)
    # Create label widget for output
    output_label = tk.Label(root, text="The output:")
    output_label.grid(row=7, column=0)
    output_value = tk.Label(root, text = out, width= 50)
    output_value.grid(row=7, column = 1, columnspan=2, sticky="w")



    
submit_button = tk.Button(root, text="Excute", command=submit)
submit_button.config(width=27)
submit_button.grid(row=5, column=1, pady=10, padx = 10)


root.mainloop()
