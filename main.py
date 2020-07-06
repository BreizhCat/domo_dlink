#!/opt/bin/python3
 
__author__ = "Yann LEROUX"
__version__ = "1.0.0"
__email__ = "yleroux@gmail.com"

from dlinkdcs import DlinkDCSCamera
import sys
import json

def main():
    full_path = "/usr/local/domoticz/var/scripts/dlink/"
    with open(full_path + 'code.json') as param_data:
        data = json.load(param_data)
    
    dcs = DlinkDCSCamera(data['ip'], data['user'], data['password'])
    if sys.argv[1] == '--on':
        dcs.enable_motion_detection()
   
    if sys.argv[1] == '--off': 
        dcs.disable_motion_detection()

main()