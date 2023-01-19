#!/bin/bash

# You have audit log file which has ssh connection logs to your server. 
# However some invalid users try to connect your system. 
# You have been assigned a task to find their names and 
# how many times have they tried to attack your system. 
# Please find it and put it into the `invalid_user.sh`file.

#grep -Eio "input_userauth_request: invalid user .+ " auth.log | awk '{print $4}' | sort | uniq -c > invalid_user.sh
# or
#cat auth.log | grep -i invalid | grep -i Failed | awk '{print $9 " " $10 " " $11}'| sort|uniq -c | nl | tee invalid_user.sh
# or
#awk '/Invalid user/' auth.log | awk -F"]: " '{print $2}' | awk -F" " '{print $3}' | sort | uniq -c > invalid_user.sh
# or
#cat auth.log | grep "Failed password for invalid user" | awk '{print $11}' | sort | uniq -c > result.txt

grep "invalid user" auth.log | awk '{print $11}' | sort | uniq -c > invalid_user.sh