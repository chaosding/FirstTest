import netifaces
import sys,os
import commands
import subprocess

#if_connect=netifaces.gateways()['default'][netifaces.AF_INET][1]
#print if_connect

#test=netifaces.interfaces()
#print test
cmd="powershell -Command  \"&{ Get-WmiObject win32_networkadapter | select name, pnpdeviceid, MACaddress | Where-Object \
	{ $_.PnpDeviceID -Match 'PCI*' } | select MACAddress }\""
	
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print out
out.replace(" ","")
print out


