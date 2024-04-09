#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = open("mbox.txt", "r")
count={}
for line in fname:
    #print(line)
    if line.startswith("From "):
        spliting = line.split( )
        email=spliting[1]
        count[email]=count.get(email,0)+1
        most_prolific_sender = max(count, key=count.get)
#Print the email address of the most prolific sender and their count of emails:
print(most_prolific_sender, count[most_prolific_sender])
