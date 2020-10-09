import sys
import subprocess
from os.path import expanduser
import pathlib
import os


pwd = os.path.dirname(os.path.abspath(__file__))

def userHome():
	return expanduser("~")


def defeultDesktopEntryParams():
	return [
		["Version","1.0"],
		["Name","Add Menu"],
		["Comment","Adicions laçador ao menu"],
		["Icon",pwd+"/addmenu.png"],
		["GenericName","add menu"],
		["Exec","/usr/bin/addmenu"],
		["Terminal","false"],
		["X-MultipleArgs","false"],
		["Type","Application"],
		["Categories","Application;tools;"],
		["MimeType","text/plain;"],
		["StartupNotify","true"],
	]

def saveDesktopEntry(fName, params):

	content="[Desktop Entry]\n"
	for linha in params:
		content = content+ linha[0]+"="+linha[1]+"\n"

	print(content)
	with open(userHome()+"/.local/share/applications/"+fName+".desktop", 'w') as f:
		f.write(content)

