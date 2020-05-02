#10.3. Alternative File Reading Methods






#1 Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.


filevar=open("school_prompt2.txt","r")
ch=filevar.read()
num_char=0
for i in ch:
    num_char=num_char+1
print(num_char)    
filevar.close()


#2 Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.

filevar=open("travel_plans2.txt","r")
line=filevar.readlines() #note readline and readlines
num_lines=0
for i in line:
    print(i.strip())
    num_lines=num_lines+1
print(num_lines)    

#3 Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

filevar=open("emotion_words2.txt","r")
ch=filevar.read(40)
first_forty=""
for i in ch:
    first_forty=first_forty+i
print(first_forty)    


#10.4. Iterating over lines in a file
olypmicsfile = open("olypmics.txt", "r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()


#10.8. Writing Text Files¶


filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10]) #10 chracters including new lines
infile.close()





#10.6. Using with for Files

with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
# continue on with other code



#10.7. Recipe for Reading and Processing a File¶

fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4


