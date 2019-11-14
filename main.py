from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import sparql

search = input("Search:")
processedWords = []
words = nltk.word_tokenize(search)
sTwords = stopwords.words('english')

#print(words)
#Removing stopwords
flag=0
for word in words:
    if word not in sTwords:
        if(flag==0):
            flag=1
        else:
            flag=2
        processedWords.append(word)
    else:
        if(flag==2):
            processedWords.append(word)

#print(processedWords)
tagged_words = nltk.pos_tag(processedWords)
#print(tagged_words)
print('Searching...')

#What <stopword> <attribute> of <term>
if (tagged_words[0][0] == 'What'):
    term = ''
    #term+=tagged_words[2][0]
    attribute=''
    #attribute+=tagged_words[1][0]
    i = 0
    f = 0
    for word in tagged_words:
        if(f):
            term+=' '+word[0]
        else:
            if(word[0]=='of'):
                f=1;
            elif(word[0]!='What'):
                attribute+=' '+word[0]
    attribute=attribute[1:]
    term=term[1:]
    #print(tagged_words)
    #print(attribute)
    #print(term)
    #print(attribute)
    sparql.whatIs(term,attribute)
#List each country with <attribute> <greater/lesser than >
#if(tagged_words[0][1]=='')
    
if(tagged_words[0][0]=='List'):
    attribute=''
    comp=0  #greater=1,lesser=-1,0 otherwise
    limit=0 
    i=0
    f=0
    for word in tagged_words:
        i+=1
        if(i<4):
            continue
        if(word[0]!='greater' and word[0]!='lesser' and word[0]!='than'):
            if(not f):
                attribute+=' '+word[0]
            else:
                limit=word[0]
        elif(word[0]=='greater'):
            comp=1
        elif(word[0]=='lesser'):
            comp=-1
        elif(word[0]=='than'):
            f=1
    attribute=attribute[1:]
    #print("listEach")
    sparql.listEach(attribute,comp,limit)
    #print(attribute)
    #print(comp)
    #print(limit)

if(tagged_words[0][0]=='How'):
    attribute=''
    comp=0  #greater=1,lesser=-1,0 otherwise
    limit=0 
    i=0
    f=0
    for word in tagged_words:
        i+=1
        if(i<5):
            continue
        if(word[0]!='greater' and word[0]!='lesser' and word[0]!='than'):
            if(not f):
                attribute+=' '+word[0]
            else:
                limit=word[0]
        elif(word[0]=='greater'):
            comp=1
        elif(word[0]=='lesser'):
            comp=-1
        elif(word[0]=='than'):
            f=1
    attribute=attribute[1:]
    #print("listEach")
    sparql.howMany(attribute,comp,limit)
    #print(attribute)
    #print(comp)
    #print(limit)

