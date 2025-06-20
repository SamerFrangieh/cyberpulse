import nmap

# Optional: Map some common ports to services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def run_nmap(target):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target, arguments='-T4 -sV -F')  # -sV for service version detection
    result = []

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                result.append({
                    'port': port,
                    'state': service.get('state'),
                    'name': service.get('name', ''),
                    'product': service.get('product', ''),
                    'version': service.get('version', ''),
                    'cpe': service.get('cpe', ''),
                    'common_name': COMMON_PORTS.get(port, '')
                })
    return result
