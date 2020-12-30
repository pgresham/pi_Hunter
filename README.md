# pi_Hunter

Tool to scan ip range for default credentialed Raspberry pi

Version 1.0

---
Software Dependencies:
--------
To run this you must have Python 3.x with the pexpect package installed.
The current version is written for *nix systems.

---
Using pi HUNTER:
--------

Pretty straightforward, select whether you want to search IPv4 or IPv6 addresses, then enter the start and end addresses for the block. pi HUNTER checks the default username 'pi' and password 'raspberry' on each address' port 22 and returns IPs that contain a default credentialed (and therefore vulnerable) pi. 


