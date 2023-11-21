# . Write a program for DNS lookup. Given an IP address input, it should return URL and vice
# versa.
import socket
def ip_to_domain(ip_address):
        domain = socket.gethostbyaddr(ip_address)
        return domain[0]

def domain_to_ip(domain_name):
        ip_address = socket.gethostbyname(domain_name)
        return ip_address

ip_address = '142.250.66.4'
domain_name = 'www.facebook.com'

print("Domain for IP", ip_address,  ':',  ip_to_domain(ip_address))
print(f"IP for Domain", domain_name, ':', domain_to_ip(domain_name))
