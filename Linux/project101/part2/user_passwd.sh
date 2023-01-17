#!/bin/bash
#
# This script creates a new user on the local system.
# You will be prompted to enter the username (login), the person name, and a password.
# The username, password, and host for the account will be displayed.

# Make sure the script is being executed with superuser privileges.


# Get the username (login).
# read -p "please enter your username: " username

# # Get the real name (contents for the description field).
# read -p "please enter your name : " name

# # Get the password.

# read -p "please enter your password"

# # Create the account.
# sudo useradd $username
# sudo passwd $username

# Check to see if the useradd command succeeded.
# We don't want to tell the user that an account was created when it hasn't been.

# Set the password.

# Check to see if the passwd command succeeded.

# Force password change on first login.

# Display the username, password, and the host where the user was created.

# Script to create new user account and automatically generate password

# Check for root user
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Check for input arguments
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 username comments"
    exit 1
fi

username=$1
comments=$2

# Generate random password
password=$(date +%s%N | sha256sum | head -c32)

# Create new user account with generated password
useradd -c "$comments" -m $username
echo $username:$password | chpasswd

# Force password change on first login
chage -d 0 $username

echo "User: $username has been created with password: $password"