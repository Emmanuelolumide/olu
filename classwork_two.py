#this program sort out and print out the 5 most common words used
thefile = input('Enter file name: ')
openfile = open(thefile) #this opens the file
di = dict() #dicitionary
for line in openfile:
	line = line.split()
# splits the text and count it
	for word in line:
		di[word] = di.get(word, 0) + 1
		
ls = list()
for key, value in di.items(): #for every key and value in the dicitionary
	newkey = (value, key) 
	ls.append(newkey) # new list was appended here
lst = sorted(ls, reverse = True) # the values were flipped
sort = lst[:5]
for key, value in sort:
	print(key, value)
			
