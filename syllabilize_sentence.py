import string
import re
import argparse
from tts_parser import *
from letters import *

def process_sentence(s):
	#s =  "Unuakumi, ayag'ciqua tuani-llu-gguq."
	exclude = string.punctuation
	exclude = exclude.replace("'|-", "")
	#exclude = exclude.replace("-", "")
	s = ''.join(ch for ch in s if ch not in exclude)
	words_to_process = s.split()
	print(words_to_process)
	s = [s.lower() for s in words_to_process]
	print(s)
	syllables = []
	for word in s:
		print(word)
		s = parser(word) ###################ERROR
		print(s)
		syllables.append(parser(word))
	return(syllables)
	#for i in words_to_process:
	#	word = i.lower()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-s", "--string", action="store_true")
	group.add_argument("-f", "--file", action="store_true")
	parser.add_argument('x',type=str, help="type in the string or the file name")
	args = parser.parse_args()
	if args.string:
		if args.x[-3:] == 'txt':
			print("You may need to use the --file flag instead.")
		print(args.x)
		s = process_sentence(args.x)
		print(s)
	elif args.file:
		with open(args.x) as file:
			for line in file:
				print(line)
	else:
	    print("Please specify whether --string or --file.")