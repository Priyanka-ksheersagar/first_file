#Open the file mbox.txt and read it line by line. When you find a line that starts with 'From ' like the following line:From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
fname = open("mbox.txt", "r")
count=0
for line in fname:
    #print(line)
    if line.startswith("From "):
        count=count+1
        spliting = line.split( )
        display=spliting[1]
        #slicing = line.slice()
        print(display)
print("There were",count,"lines in the file with From as the first word")
    