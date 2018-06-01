from spellcheck import *

with open('examplewords.txt','r') as fin:
	wordlist = []
	for line in fin:
		sentence = line.split()
		for word in sentence:
			wordlist.append(word.lower())

#check spellchecker
total = len(wordlist)
errors = 0.0
for word in wordlist:
	if spellcheck(word):
		pass
	else:
		print(word)
		errors += 1
print("{} total Errors out of {} entries, {} percent accuracy".format(int(errors), total, (total-errors)/total))
print(spellcheck('clearance'))