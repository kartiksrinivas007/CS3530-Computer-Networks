### Application Layer Protocols

---

There are 4 things defined, 
1. The type of the message REQ/RES
2. The syntax of the messages
3. The semantics of the messages
4. Rules for determinign when and how these messages are sent

A web page is basically a bunch of objects which can be either a HTML file a jPEG immage or a java applet.

Usually each page ha s abase HTML file that references other URL's or otehr objects. Each object has its own unique URL. The URL can be on some particular hostname. eg :: https:/loclahost://etc

HTTP is a <b>stateless Protocol</b>

### Persistent vs Non-persisten HTTP connections

---

Impersisten could also be done in a parallel way, this speeds things up 

there is always a 3 - way handhsake of the TCP.
This 3 way handshake first has C -S - TCP segment then S - C TCP segment - 1 RTT,
the second part is C - S Acknowledgement  + Request C - S  + Response - 1 RTT
The final is the time taken to transmit the file  - Transmission delay.

The server is the one that initialtes the close when we have impersisten HTTP, however only after the client reveives the message intactly does the connection finally close.




## HTTP 

---

There is a GETrequest and it is followed by some other requests and so-on.
The host name is in the URL, but sometimes the Host: "Address" may be different in an HTTP connection because if Web proxy( or cache servers), the connection:close indicates that it wants to close the connection (non  persstent HTTP connection is to be provided)

The User:Agent asks fo rwhat browser is actually processing thsi server ( there maybe different versions of the same file according to the USER Browser)

The Accept-Language is a negotiation header that is used to see if french is required etc, (french language or a different one if it is available else defalt).

## Forms in HTTP

The first line is called the request line, the next: separated ones are headers and then the final ones are the entity body!, this body can contain additional information you want to give in your message, or sometimes it can be asked within the UR itself, Hostname/minkeys&bananas( only if its a GET form ) else for a POST form the info will be inside the "entity body"


HEAD method will send a request but get no response object, only the headers.


## Error codes

200 OK
404 Not found 
400 Bad Request ( not able to understand)
301 Moved Permanently
505 HTTP V not supported.
