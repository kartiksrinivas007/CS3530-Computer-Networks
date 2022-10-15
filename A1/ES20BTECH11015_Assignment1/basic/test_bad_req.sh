##/bin/bash

bash h1-arp.sh
echo "Trying a bad GET Request"
printf "%s\n%s" "GET /assignment1?request=key8 HTTP/1.1" "q" | python client.py
echo "Trying a bad DELETE Request"
printf "%s\n%s" "DELETE /assignment1?request=key8 HTTP/1.1" "q" | python client.py