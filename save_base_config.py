

# developed by Gabi Zapodeanu, TSA, Global Partner Organization

from cli import cli

import os
os.chdir('/bootflash/Unauth_config_rollback')

# add additional vty lines, two required for EEM
# save baseline running configuration

cli('configure terminal ; line vty 0 15 ; length 0 ; transport input ssh ; exit')

output = cli('show run')
filename = 'base-config'

f = open(filename, "w")
f.write(output)
f.close

print("End Application Run Save Base Configuration")