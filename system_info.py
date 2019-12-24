#!/usr/bin/python3

# A system Information Gathering Script
import subprocess

def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print("Gathering system information with %s command:\n" %uname)
    subprocess.call([uname, uname_arg])


def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering diskspace information %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])

# Main function that call other functions
def main():
    uname_func()
    disk_func()

main()
