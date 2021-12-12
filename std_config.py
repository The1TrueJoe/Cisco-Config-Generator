# STD Comment Header
def std_comment_header():
    return '''
            !\n
            ! Config Script By 14-4514\n
            ! Autognerated by github.com/The1TrueJoe/Cisco-Config-Generator\n
            !\n
            '''

# Enter config mode
def enter_config():
    return '''
            enable\n
            config t\n
            '''

# Standard config options
def std_config():
    return '''
            no ip domain lookup\n
            service password-encryption\n'''

# Set the hostname
def set_hostname(hostname):
    return "hostname " + hostname + "\n"

# Set the enable password
def set_enable_password(password):
    return "enable secret " + password + "\n"

# Close standard
def close_std_config():
    return "!\n"

# End config and save
def save():
    return '''
            !\n
            !\n
            !\n
            exit\n
            copy run start'''