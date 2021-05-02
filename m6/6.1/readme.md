## Task 6.1

I created 2 VMs on Ubuntu Server 16.04. VM1 (server16.04) has 2 network adapters: NAT and Internal. VM2 (server16.04 Clone) has only Internal adapter. Internal network is myDHCP, but I will assign addresses manually later.

<p><img src="./screenshots/vm1adapt.png"></p>

<p><img src="./screenshots/vm2adapt.png"></p>

Next, I configured interfaces on VM1 and VM2 in `etc/network/interfaces`.

VM1:

<p><img src="./screenshots/interfaces1.png"></p>

* enp0s3 - NAT adapter
* enp0s8 - Internal

VM2:

<p><img src="./screenshots/interfaces2.png"></p>

* enp0s3 - Internal

Here, the default gateway is the address of enp0s8 of VM1.

Next, I enabled IP forwarding on VM1 by uncommenting line in `etc/sysctl.conf`:

<p><img src="./screenshots/ip_forward.png"></p>

After that, I created new rules in `iptables` to forward packets:

<p><img src="./screenshots/iptables.png"></p>

<p><img src="./screenshots/masq.png"></p>

Now, lets test connection:

ping from VM2 to host:

<p><img src="./screenshots/pingHost.png"></p>

ping from VM2 to internet (8.8.8.8):

<p><img src="./screenshots/pingGoogle.png"></p>

To find out which recource corresponds to which IP, `nslookup` command can be used:

<p><img src="./screenshots/nslookupGoogle.png"></p>

`dig` or `nslookup` can be used to get IP from domain name.

<p><img src="./screenshots/digEpam.png"></p>

<p><img src="./screenshots/nslookupEpam.png"></p>

Here is default gateway and routing table (`netstat -rn`) of host:

<p><img src="./screenshots/gw.png"></p>

<p><img src="./screenshots/routing_table.png"></p>

I tested `traceroute` command with -I flag (ICMP) from VM2:

<p><img src="./screenshots/traceroute.png"></p>