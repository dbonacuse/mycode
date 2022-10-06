#!/bin/bash

prompt(){
echo -n "Enter your  username: "
read username

echo -n "Enter the user's group : "
read group
}

createuser(){
sudo useradd  "$username"
echo "$username has been created."
sleep 1
sudo groupadd $group
echo "$group has been created."
sleep 1
sudo usermod -aG $group $username
echo  "$username has been added to $group"
}

quit(){
    echo "If you would like to quit, please type the word exit."
    read quit
}

while [ "$quit" != "exit" ]
do
    prompt
    createuser
    quit
done
echo "Thank you for adding a user and/or group. Have a blessed day."
