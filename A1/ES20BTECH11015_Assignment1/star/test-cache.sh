#!/bin/bash

bash h1-arp.sh
echo "Testing case where the Key is in the cache"
printf "%s\n%s" "GET /assignment1?request=key1 HTTP/1.1" "q" | python client.py
echo "Enter \"n\" for next test where Key is not in cache"
read prompt
echo $prompt
if [[ $prompt == "n" ]]; then
	echo "Sending GET request for key2 which is not in Cache"
	printf "%s\n%s" "GET /assignment1?request=key2 HTTP/1.1" "q" | python client.py
fi
echo "Enter \"n\" for next PUT test"
read prompt
echo $prompt
if [[ $prompt == "n" ]]; then
	echo "Sending PUT request"
	printf "%s\n%s" "PUT /assignment1/key7/val7 HTTP/1.1" "q" | python client.py
fi
echo "Enter \"n\" for next DELETE test"
read prompt
echo $prompt
if [[ $prompt == "n" ]]; then
	echo "Sending DELETE request"
	printf "%s\n%s" "DELETE /assignment1/key7 HTTP/1.1" "q" | python client.py
fi
echo "Ending tests"
