import std_config as config
import simple_interfaces as interface

def header():
    print("Cisco Device Configuration Generator")
    print("By GSSM Cyberpatriot Team 14-4514")
    print("See github.com/The1TrueJoe/Cisco-Config-Generator")
    print("....\n\n\n")

def main():
    # Print Header
    header()

    # Hostname and File Name
    print("Enter Hostname:")
    hostname = input()

    # Open file
    file = open(hostname, "x")

    # STD Configuration Block
    file.write(config.std_comment_header())
    file.write(config.enter_config())
    file.write(config.std_config())
    file.write(config.set_hostname(hostname=hostname))
    file.write(config.close_std_config)

    # Get Interface Count
    print("Do you want to configure interfaces y|N")
    config_interfaces = input().upper() == "N"

    # Interface Config Looop
    while(config_interfaces):
        # Inter
        print("Enter interface name: ('N' to cancel)")
        interface_name = input()

        # Configure interfaces
        if (interface_name.upper() != "N"):
            # Init Interface Config
            interface.initiate_config(interface_name=interface_name)

            # Set the ip
            print("What is " + interface_name + "'s ip:")
            ip = input()

            # Set the subnet
            print("What is " + interface_name + "'s subnet (aaa.bbb.ccc.ddd):")
            subnet = input()

            # Push address config
            interface.config_ip(ip=ip, subnet=subnet)

            # Request manual configurations
            print("Enter manual config y|N")
            man_config = input().upper() == "y"

            # Manual configuration loop
            while (man_config):
                # Input
                print ("Manual Config Option: ('N' to cancel)")
                console_input = input()

                # Exit case
                if (console_input == 'N'):
                    man_config = False

                else:
                    # Write input
                    file.write(console_input)

                    # Loop
                    print("Enter manual config y|N")
                    man_config = input().upper() == "y"

        else:
            # Exit interface configuration
            config_interfaces = False
            print("Interface basic configuration finished")
        

    file.close()
    
if __name__ == "__main__":
    main()
