#!/bin/bash
#prompt for input
prompt(){
echo "What is the user's name?"
read user

echo "What is the user's group"?
read group
}

#create the user and add group
makeUser(){
echo "Now creating new user!"
sudo useradd $user
echo "$user created!"
sudo groupadd $group
echo "Now adding $user to $group"
sudo usermod -aG $group $user
echo "User added to group!"

#quit application
quit(){
echo "Would you like to quit?"
read quit
}
done
