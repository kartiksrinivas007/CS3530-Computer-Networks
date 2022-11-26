
## Simplest Scenario
---
One router and infinite buffer capacity.
input and output link capacity of $R$

Say that the Host's are sending at a particular rate then
let A an dB send at the rate $\lambda$
and $\lambda = R/2$, because of the time to process a packet (if there are delays)
then the packet(queueing) delay will begin to increase. and will tend to infinity as the 
$2\lambda \rightarrow R$

If the buffer size is infinite, then the throughput (the one whhcih the sender and the receiver receive) is equal to $\lambda_{in}$

One router, finite buffer, the **TCP** will send at  a higher throughput than the application layer( because of the re-transmission rates)


There are three cases, the ideal, the un-needed duplicates and packet loss
in ideal case , no delays then $\lambda_{in} = \lambda_{out}$
Then the next case is where the $\lambda_{out}$ < $\lambda_{in}$

