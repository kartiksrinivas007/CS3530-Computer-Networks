#!/bin/bash

bash h1-arp.sh
while [[ $input != "q" ]]; do
	echo "Enter G for Get, P for PUT and D for DELETE request, or enter q to quit"
	read prompt
	input=$prompt
	if [[ $prompt == "G" ]]; then
		echo "Enter the Key value for GET Request"
		read Key
		echo "Sending GET request for $Key"
		printf "%s\n%s" "GET /assignment1?request=$Key HTTP/1.1" "q" | python client.py
	elif [[ $prompt == "P" ]]; then
		echo "Enter Key for PUT request"
		read Key
		echo "Enter value FOR PUT REQUEST"
		read value
		echo "Sending PUT Request"
		printf "%s\n%s" "PUT /assignment1/$Key/$value HTTP/1.1" "q" | python client.py
	elif [[ $prompt == "D" ]]; then
		echo "Enter Key that is to be deleted"
		read Key
		echo "Sending DELETE request"
		printf "%s\n%s" "DELETE /assignment1/$Key HTTP/1.1" "q" | python client.py
	elif [[ $prompt == "q" ]]; then
		echo "Ending Tests"
	fi
done


