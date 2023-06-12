import subprocess , optparse , re
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to help")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse_object.parse_args()

#
def mac_changer(user_interface,user_mac_address):

    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(user_interface):
    ifconfig = subprocess.check_output(["ifconfig",user_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    
    if new_mac:
        return new_mac.group(0);
    else :
        return None


(user_inputs,arguments) = get_user_input();
mac_changer(user_inputs.interface,user_inputs.mac_address)
finalized_mac =control_new_mac(str(user_inputs.interface))

if finalized_mac == user_inputs.mac_address:
    print("Success")
else :
    print("Error")

