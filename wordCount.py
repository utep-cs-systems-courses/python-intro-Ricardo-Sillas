import sys
import re
import os

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()
    
f = open(textFname, 'r')
dict = {}
for line in f:
    for word in re.split('\W+', line):      # Split words
        if word.lower() in dict:            # Word in dict
            dict[word.lower()] += 1
        elif word != "":                    # Word not in dict
            dict[word.lower()] = 1
        
sortDict = sorted(dict)

with open(outputFname, 'w') as writer:  #write to file from dict
    for i in sortDict:
        numWord = i + " " + str(dict[i]) + "\n"
        writer.write(numWord)