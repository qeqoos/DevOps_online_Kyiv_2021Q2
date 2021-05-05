## Task 6.2

I cloned VM2. Now, I have 3 VMs: one with NAT + Internal and two with internal interfaces.
First, I configured DHCP using VBoxManage. I need to create dhcpserver:

<p><img src="./screenshots/vboxmanageDHCP.png"></p>

I chose every internal adapter to use `myDHCP`. In VMs, in `/etc/network/interfaces/` change static addresses of interfaces to dhcp.
Restart interfaces (ifdown, ifup).

<p><img src="./screenshots/internalDHCP.png"></p>

Result of VBoxManage approach:

<p><img src="./screenshots/vboxmanageSHOW.png"></p>

Next, I configured `dnsmasq` service. I made VM1 Internal interface static IP, then I uncommented some strings in `/etc/dnsmasq.conf`. 

* interface=enp0s8 (internal interface)
* dhcp-range

<p><img src="./screenshots/dhcpmasq1.png"></p>

To demonstrate, in VM settings, I chose `intnet`.

<p><img src="./screenshots/internalINTNET.png"></p>

<p><img src="./screenshots/dhcpmasq2.png"></p>

Next, I configure DNS on VM1, I uncomment `prepend domain-name-servers` line in `/etc/dhcp/dhclient.conf` and check `/etc/resolv.conf` nameserver.

<p><img src="./screenshots/dns2.png"></p>

<p><img src="./screenshots/dns3.png"></p>

Also, for further testing I enable packet forwarding on VM1:

<p><img src="./screenshots/dns1.png"></p>

I check the work of DNS-server on VM2 and VM3 by using `dig`:

<p><img src="./screenshots/dnstest.png"></p>
