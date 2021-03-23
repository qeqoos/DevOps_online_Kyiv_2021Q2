## Part 1: Hypervisors

The most popular hypervisors are **Virtual Box** and **VMware Workstation**.

###### Differences
**VMvare Workstation**, unlike **Virtual Box**, is not free, thus has better client support. 
It will provide better compatibility with VMware servers and data management tools.
**Virtual Box** is open-source, can be installed on Windows, Linux, Mac OS X and Solaris.
**VMvare Workstation** can be installed only on Windows and Linux.
**Virtual Box** consumes less resources. 
**VMvare Workstation** has more tools for virtual networking and integration for test environments.
**VMvare Workstation** is better for enterprice use, **Virtual Box** is better for learning and "home" usage.

## Part 2: Work with Virtual box

<p>The first step was to install Virtual box and create virtual machine.<br>
I chose ubuntu, gave it 3 GB of RAM, 2 processors and 15 GB of hard drive.
</p>

<img src="./screenshots/1.4.1.png" width="900" height="900">

<p>Here it is up and running:</p>

<img src="./screenshots/1.4.2.png">

<p>Next step is cloning virtual machine.</p>

<img src="./screenshots/1.5.png">

<p>Grouped them up to apply different commands or changes simultaneously.</p>

<img src="./screenshots/1.6.png" width="900" height="900">

<p>I changed virtual machine a little bit and took snapshot, therefore created snapshot tree.<br>
This allows me to restore previous states of virtual machine.
</p>

<img src="./screenshots/1.7.png">

<p>I exported first VM and created .ova file, which stands for Open Virtual Appliance.</p>

<img src="./screenshots/1.8.1.png" width="900" height="900">

<p>Then, I imported newmade file into new guest OS.</p>

<img src="./screenshots/1.8.2.png" width="900" height="900">

<p>Next task was to explore configuration options.<br>
I configured the USB flash drive to connect to the VM.<br>
You can manually choose device, or set up filter.
</p>

<img src="./screenshots/2.2.1.png" width="900" height="900">

<p>Here you can see it in my guest OS.</p>

<img src="./screenshots/2.2.2.png">

<p>I created shared folder to exchange files between host and guest.<br>
Option <code>--automount</code> just automatically mounts shared folder on OS startup.
</p>

<img src="./screenshots/2.3.1.png" width="800" height="50">

<p>Here it is in action.</p>

<img src="./screenshots/2.3.2.png">

<p>Next part is configuration of network mods. I tested 4 network modes: </p>

<p>
<img src="./screenshots/network_modes.png" width="800" height="150">
</p>

For further tests:
* Host address - <code>192.168.0.107</code>
* First VM - <code>192.168.0.101</code>
* Second VM - <code>192.168.0.102</code>
* First VM in host-only mode - <code>192.168.56.101</code>
* Second VM in host-only mode - <code>192.168.56.102</code>

<p>Host-only mode. Host can ping guests and vice virsa.<br>
Guests can ping each other, but cannot access internet.
</p>

<p>Here we can see, that guests can ping host.</p>

<img src="./screenshots/2.4.1hostonly.png">

<p>Host can ping second VM. First VM can ping second VM.<br>
Second VM cannot ping <code>8.8.8.8</code> (google dns).
</p>

<img src="./screenshots/2.4.2hostonly.png">

<p>Internal mode. Guest VMs only can ping each other.<br>
We can see, that there were attempts to ping host and google.com.
</p>

<img src="./screenshots/2.4internal.png">

<p>Bridged mode. VMs can ping each other, host and google.com.<br>
Here first VM pings second VM.
</p>

<img src="./screenshots/2.4.1bridged.png">

<p>Access to the network.</p>

<img src="./screenshots/2.4.2bridged.png">

<p>Host pings second VM.</p>

<img src="./screenshots/2.4.3bridged.png">

<p>NAT mode. VMs cannot ping each other.<br>
VMs can ping host and google.com.</p>

<img src="./screenshots/2.4.1NAT.png">

<p>I also worked with Virtual box through command line.<br>
Here I tried basic commands for starting VM, output list of VMs.
</p>

<img src="./screenshots/3.2.1.png" width="680" height="200">

<p>Output of command <code>showvminfo</code>.</p>

<img src="./screenshots/3.2.2.png" width="900" height="900">

## Part 3: Work with Vagrant

<p>I downloaded the last version of Vagrant and installed it.<br>
I created folder and initialized the environment for Vagrant box with <code>init hashicorp/precise64</code>.<br>
After that, start Vagrant VM with <code>vagrant up</code>.
</p>

<img src="./screenshots/vagrant1.png" width="900" height="900">

<p>Connection to Vagrant VM has been established through SSH using <strong>MobaXtrem</strong>.<br>
After successful connection I executed command <code>date</code> to ensure, that everything works.
</p>

<img src="./screenshots/vagrant2.png" width="1000" height="700">

<p>After testing, I stopped and deleted VM.</p>

<img src="./screenshots/vagrant3.png" width="600" height="80">

<p>To create my own vagrant box, firstly I created new VM - Ubuntu Server.<br>
Then I opened powershell and typed <code>vagrant package --base 'LinuxVagrant' --output PavelsBox_template</code>.<br>
This command creates template of my VM. Now I can create VMs off of my template using vagrant. 
</p>

<img src="./screenshots/vagrant4.png" width="900" height="900">