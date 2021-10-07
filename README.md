# BeyDos
A DDoS tool meant to test Minecraft servers and small websites

USE IF GIVEN PERMISSION, I AM NOT RESPONSIBLE FOR ANY DAMAGES, LEGAL ISSUES, OR LAWSUITS.

Currently, this tool is in Work In Progress, but it will soon be released.

Attacks:

UDP: Great For Testing Minecraft Servers, Floods 1024 Bytes Of Data.

HTTP GET: Great For Testing Websites, Floods HTTP Get Requests

### How to use:

-i --ipv4: The IP You Want To Attack, Necessary for the script to work

-p --port: the port for the IP, if left blank, defaults to 80.

-m --mask: masks IP, use if you want a masked attack.

-h --HTTP: enables HTTP attack, needs argument like the rest of these

### How To Install Tutorial:

download this repo, extract it, and cd to it.
then, do this command:
```
pip install -r requirements.txt 
or
pip3 install -r requirements.txt
```
afterwards, when it is done, do this.
```
python beydos.py -p (port) -i (ip/address)
or
python3 beydos.py -p (port) -i (ip/address)
```
> make sure to not include (port) or (ip/adress), replace them with the port and ip  that you wish to test.
