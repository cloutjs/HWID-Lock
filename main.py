import subprocess, requests, time, os
import sys




hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

r = requests.get('https://pastebin.com/(paste)')

try:
    if hwid in r.text:
        pass
    else:
        print('[ERROR] FAILED TO CONNECT TO DATABASE') 
        time.sleep(5)
        sys.exit()
except:
    print('[ERROR] FAILED TO CONNECT TO DATABASE')
    print()
    print("CLOSING PROGRAM")
    time.sleep(5) 
    sys.exit() 
    
print('Welcome')
input()