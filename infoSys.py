#!/usr/bin/env python


import subprocess

#System Info

def sys_info():
	uname = 'uname'
	uname_arg  = '-a'
	print "###########################"
	print "Gathering System Information with command: %s \n" % uname
	subprocess.call([uname,uname_arg])



#Disk info
def disk_func():


	disk = 'df'
	disk_arg = '-h'
	print "##########################"
	print "Gathering Disk Information with command: %s \n" % disk 
	subprocess.call([disk,disk_arg])


#Main Programm


def main():
	sys_info()
	disk_func()


if __name__ == "__main__":
	main()
	
	
