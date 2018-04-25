# **Unauthorized Configuration Changes Rollback**

This repo is used for the Partner Community demo : Unauthorized Configuration Changes Rollback

 - Equipment needed: IOS-XE devices, Catalyst 9000 switch, CSR1000V 
 - Guest Shell configuration, git installation to download the code from GitHub
 - Code tested on a CSR1000v DevNet Sandbox running 16.6.1: IOS XE Programmability NETCONF-RESTCONF-YANG

Files included:
 - config_applets.txt - Sample EEM configuration required on the network device
 - base-config - file that will hold you baseline configuration
 - current-config - file that will hold updated running configuration
 - diff - file with the delta between the baseline and the changed configurations
 - save_base_config.py - script that will do the initial setup of the device
 - unauth_config.py - the script that will rollback any configuration changes 