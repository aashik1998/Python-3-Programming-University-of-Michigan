#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

filevar=open("travel_plans.txt","r")
ch=filevar.read()
num=0
for i in ch:
    num=num+1
    #print(ch)


#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
filevar=open("emotion_words.txt","r")
line=filevar.readlines()
num_words=0
for i in line:
    splited=i.split()
    num_words=num_words+len(splited)

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
filevar=open("school_prompt.txt","r")
line=filevar.read(30)
beginning_chars=""
for i in line:
    beginning_chars=beginning_chars+i


#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

filevar=open("school_prompt.txt","r")
line=filevar.readlines()
three,b=[],[]
for i in line:
    b=i.split()
    three.append(b[2])


# Create a list called emotions that contains the first word of every line in emotion_words.txt.
filevar=open("emotion_words.txt","r")
line=filevar.readlines()
emotions,b=[],[]
for i in line:
    b=i.split()
    emotions.append(b[0])
#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

filevar=open("travel_plans.txt","r")
ch=filevar.read(33)
first_chars=""
for i in ch:
    first_chars=first_chars+i


# Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

filevar=open("school_prompt.txt","r")
line=filevar.readlines()
p_words,b=[],[]
for i in line:
    b=i.split()
    for words in b:
        if "p" in words:
            p_words.append(words)
            
     


