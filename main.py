import socket
import argparse
def get_port_state(address, port, tcp_or_udp):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if tcp_or_udp == 'tcp' else socket.SOCK_DGRAM)
        sock.settimeout(1)
        result = sock.connect_ex((address, int(port)))
        sock.close()
        if result == 0:
            return "Open"
        else:
            return "Closed"
    except socket.error:
        return "Error"
def main():
    parser = argparse.ArgumentParser(description="nmap tool")
    parser.add_argument('-p', '--port', type=str, help="Search in range of port")
    parser.add_argument('-u', '--udp', type=str, help="Search udp port state")
    parser.add_argument('-t', '--tcp', type=str, help="Search tcp port state")
    
    args = parser.parse_args()
    
    if not (args.port or args.udp or args.tcp):
        print("Error: You should provide at least one search parameter.")
    elif '-' in args.port:
        address=""
        tcp_or_upd=''
        if args.udp:
            address=args.udp
            tcp_or_upd='udp'
        elif args.tcp:
            address=args.tcp
            tcp_or_upd='tcp'
        start=int((args.port).split('-')[0])
        end=int((args.port).split('-')[1])
        for u in range(start,end+1):
            print("Port",u,get_port_state(address,u,tcp_or_upd))
    else:
        address=""
        tcp_or_upd=''
        if args.udp:
            address=args.udp
            tcp_or_upd='udp'
        elif args.tcp:
            address=args.tcp
            tcp_or_upd='tcp'
        print("Port",args.port,get_port_state(address,args.port,tcp_or_upd))
    
                
        
if __name__ == '__main__':
    main()


    