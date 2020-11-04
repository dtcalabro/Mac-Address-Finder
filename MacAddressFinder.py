"""
This program finds the mac address of a device in question that is on the same network as you.
"""
from getmac import get_mac_address, getmac

# Main loop where the magic happens
while True:
    # Constants
    ip_mac = get_mac_address(ip = '192.168.0.1')

    # We ask the user for the IP of the device
    device_ip = input('[*] Enter the IP of the device: ')

    # The next portion is used to display the mac address and/or tell the user that the device cannot be 
    # found if the mac address returned is "ff:ff:ff:ff:ff:ff"
    mac_addy = str(getmac.get_mac_address(ip = device_ip))
    if mac_addy != 'ff:ff:ff:ff:ff:ff':
        # If the device can be found, then we print out the mac address
        print('[*] Mac address of '+ str(device_ip) + ' is: ' + (mac_addy))
    elif mac_addy == 'ff:ff:ff:ff:ff:ff':
        # If the device cannot be found, then we print out that the device cannot be found
        print('[*] Device cannot be found!')

    # Below we ask the user if they have another device that they would like to find the mac address of
    ask_go_again = input('[*] Would you like to find another mac address?: ')
    if ask_go_again == 'Yes' or ask_go_again == 'yes':
        # If they answer yes, then we loop back to the beginning
        continue
    elif ask_go_again == 'No' or ask_go_again == 'no':
        # If they answer no, then we end code execution
        break
    else:
        # If they do not answer yes or no, then we quit anyways
        print('[*] I am not too sure what you want to do, so I will quit anyways!')
        break
