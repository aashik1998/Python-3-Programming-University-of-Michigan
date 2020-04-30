#Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a=[]
a=scores.split(" ")
a_scores=0
for i in a:
    if int(i)>89:
        a_scores=a_scores+1

#

#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org=org.split(" ")
acro=""
for i in org:
    if i not in stopwords:
        i=i[:1].upper()
        print(i)
        acro=acro+i
     
#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent=sent.split(" ")
acro1=[]
acro=""
#print(sent)
for i in sent:
    if i not in stopwords:
        i=i[:2].upper()
        acro1.append(i)
        print(i)
for i in acro1:
    acro=acro+i+". "
acro=acro[:-2] 
print(acro)        


#A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
r_phrase=''.join(reversed(p_phrase)) 
print(r_phrase)
a=p_phrase.split(" ")
b=""
for i in a:
    b=b+i
b=b.lower()    
print(b)
c=r_phrase.split(" ")
d=""
for j in c:
    d=d+j 
d=d.lower()    
print(d)
if b==d:
    print("it is a pallindrome")
