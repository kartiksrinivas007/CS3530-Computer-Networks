# Assignment -1

---

## Request Format


> `GET /assignment1?request=key1 HTTP/1.1`

> `PUT /assignment1/key1/val1 HTTP/1.1`

> `DELETE /assignment1/key1 HTTP/1.1`

## How to run Basic Topology

---

### Option 1-  Run the Shell Script <i>run_tests.sh</i> 

Run it on the Xterm window of node h1. Node h1 is the client , node h2 is the server.
```bash
bash run_tests.sh
```
### Option 2 - Enter the Entire request Manually

You can do this by simply running the python file

```
bash h1-arp.sh
python client.py
```

## How to run the Star Topology 

---

First setup nodes H2 and H3 using mininet and running the bash scripts.
Then you can run the same Shell Script <i>run_tests.sh</i> on the Xterm window for Node h1.

### Option -1 Use a Shell Script for easy Entering of Keys and Values
```bash
bash run_tests.sh
```
### Option - 2 Enter the Entire Request Manually

```bash
bash h1-arp.sh
python client.py
```

## Where are the PCAP Files?

---

<b> Pcap files for each topology are under the folder <i>Real-pcaps</i></b>
Each of which contain the Pcap traces for the question along with the three pcap traces of the three experiments for the table under the folder <i>GET-Request-Analysis</i>.

## Any differences Between Both the Options of Running?
---
d
Yes the differences are that the Shell script kills the connection each time you provide a Prompt. This is like an <b>Impersistent HTTP</b> request
However, if you run the python file, then the inputs are all over the same connection. This is a <b>Persistent Model</b>.

<b>For More details please Read the Implementation Section of the report</b>
