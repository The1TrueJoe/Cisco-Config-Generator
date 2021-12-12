# Initiate the configurations
def initiate_config(interface_name):
    return "interface " + interface_name + "\n"

# Set standard config options
def std_config():
    return "no shutdown\n"

# Set the IP and subnet
def config_ip(ip, subnet):
    return "ip address " + ip + " " + subnet + "\n"

# Exit the interface config
def exit_config():
    return "exit\n!"
