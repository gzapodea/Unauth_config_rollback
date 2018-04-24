

# developed by Gabi Zapodeanu, TSA, Global Partner Organization


from cli import cli
import time
import difflib
import requests
import json
import service_now_apis
import os
os.chdir("/bootflash/PCW")


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Disable insecure https warnings


def save_config():

    # save running configuration

    output = cli('show run')
    filename = 'current_config'

    f = open(filename, "w")
    f.write(output)
    f.close

    return filename


def compare_configs(cfg1, cfg2):

    # compare two config files

    d = difflib.unified_diff(cfg1, cfg2)

    diffstr = ''

    for line in d:
        if line.find('Current configuration') == -1:
            if line.find('Last configuration change') == -1:
                if (line.find('+++') == -1) and (line.find('---') == -1):
                    if (line.find('-!') == -1) and (line.find('+!') == -1):
                       if line.startswith('+'):
                            diffstr = diffstr + '\n' + line
                       elif line.startswith('-'):
                            diffstr = diffstr + '\n' + line

    return diffstr


# main application

syslog_input = cli('show logging | in %SYS-5-CONFIG_I')
syslog_lines = syslog_input.split('\n')
lines_no = len(syslog_lines)-2
user_info = syslog_lines[lines_no]

old_cfg_fn = '/bootflash/Unauth_config_rollback/base-config'
new_cfg_fn = save_config()

f = open(old_cfg_fn)
old_cfg = f.readlines()
f.close

f = open(new_cfg_fn)
new_cfg = f.readlines()
f.close

diff = compare_configs(old_cfg,new_cfg)
print diff

f = open('/bootflash/Unauth_config_rollback/diff', 'w')
f.write(diff)
f.close

if diff != '':

    #rollback configuration
    time.sleep(5)
    cli('configure replace flash:/Unauth_config_rollback/base-config force')
    print('Config rollback successful')


print('End Application Run Unauthorized Configuration Change')
