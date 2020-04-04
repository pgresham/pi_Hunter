# pi_Hunter
Tool to scan ip range for default credentialed Raspberry pi

pi HUNTER Version 1.0


Licensed Under GNU General Public License


DISCLAIMER:
BE IT HERE KNOWN THAT THIS CODE IS FOR RESEARCH PURPOSES ONLY. IT SHOULD ONLY BE USED ON NETWORKS AND DEVICES THAT YOU OWN OR HAVE EXPLICIT PERMISSION TO ACCESS. I AM NOT RESPONSIBLE FOR ANY DAMAGE THAT COMES FROM USING THIS CODE NOR DO I CONDONE ANY MALICIOUS USAGE OR MODIFICATION OF THIS OR ANY PROGRAM I WRITE, BUT Y'ALL ALREADY KNEW THAT.

---------------------

Software Dependencies:
To run this you must have Python 3.x with the pexpect package installed.
The current version is written for *nix systems.

---------------------

Using pi HUNTER:
Pretty straightforward, select whether you want to search IPv4 or IPv6 addresses, then enter the start and end addresses for the block. pi HUNTER check the default username 'pi' and password 'raspberry' on each address and returns IPs that contain a default credentialed (and therefore stupidly vulnerable) pi. 

NOTE: As of this version, when a pi is encountered with the default username but NOT a default password, you will be in a pop-up to try another password. What you do here is up to you. The window has a Cancel button which you are invited to use.

--------------------
 
