## DNS

The DNS is a directory service, that translates the Hostname into IP addresses. It's an application layer protocol. DNS uses UDP as the transport layer protcol.


The jobs are HOst aliasing, Mail server Aliasing and then the load distribution.
the real long name is called the canonical hostname
It also does load distribution, sometimes jhostnames like cnn.com run on multiple servers ( not a single one) so many IP addresses are possible 
and in-order to provide these IP - addresses we give a set of IP addresses to the canonical hostname and the server keeps on rotating the IP addresses to keep a 
good distribution over the servers.


Problems for Single DNS server
1. The DNS server will become a singl epoint of failure
2. Millions of requests at a second
3. Cannot be close to everyone!
4. The Maintaininace and querying the Main DNS will be very hard with such a huge database !!

    usually the requests from the host to local DNS is recursive and then onwards from Root to Authoritative is all Iterative ( much faster 

```C++
$ dig www.google.com
#include<iostream>
using namespace std;
int main()
{
    cout<<"Hello World";
    return 0;
}
```
```