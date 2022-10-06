#!/bin/bash
echo -n "Enter the username: "
read username

echo -n "Enter the password: "
read -s password

adduser "$username"
echo "$password" | passwd "$username" --stdin
