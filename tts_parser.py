#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: cwtliu

import argparse
from letters import *


def parser(word):
	#doesn't account for nasal voiceless or apostrophe for beginning function case or hyphens!!!
	single_word = convert(word)
	if "'" in single_word: # more complex case of words containing apostrophes like apa'urluq this one should accent a without moving it
		return('not implemented yet')
	else:
		single_word = list(single_word)
		vowel_count = 0
		letter_count = 0
		last_vowel_index = 0
		first_vowel = True
		stress_next_vowel = False
		word_length = len(single_word)
		for i, letter in enumerate(single_word):
			if letter in v:
				if first_vowel: #rhythmic stress rule 1
					if word_length-i > 2 and single_word[i+1] in c and single_word[i+2] in c: 
						single_word[i] = letter.upper()
						stress_next_vowel = False
					elif word_length-i > 3 and single_word[i+1] in c and single_word[i+2] in v  and single_word[i+3] in v: # geminated
						single_word[i] = single_word[i].upper()
						stress_next_vowel = False
					else:
						stress_next_vowel = True
					first_vowel = False				
				elif stress_next_vowel == True and word_length-i > 1 and single_word[i+1] in v: #rhythmic stress rule 2
					single_word[last_vowel_index] = single_word[last_vowel_index].upper()
				elif stress_next_vowel == True and i > 2 and word_length-i > 2 and single_word[i-3] in v and single_word[i-2] in c and single_word[i-1] in c and single_word[i+1] in c and single_word[i+2] in v: #rhythmic stress rule 3
					single_word[last_vowel_index] = single_word[last_vowel_index].upper()
				elif stress_next_vowel == True: 
					single_word[i] = single_word[i].upper()
					stress_next_vowel = False					
				else:
					stress_next_vowel = True
				last_vowel_index = i
		single_word[last_vowel_index] = single_word[last_vowel_index].lower() #removes stress from last vowel
		print(single_word)

		### Add additional character if geminated (DOESN'T HANDLE APOSTROPHES WELL YET)
		word_length = len(single_word)
		geminated_wordform = []
		geminate_next_letter = False
		for i, letter in enumerate(single_word):
			if geminate_next_letter: # if the letter should be geminated according to next condition
				geminated_wordform.append(letter)
				geminated_wordform.append(letter)
				geminate_next_letter = False
			elif letter in v: #set the next consonant to be geminated if satisfied
				if single_word[i] == 'E':
					if i > 0 and word_length-i > 1 and (single_word[i-1] == single_word[i+1] or (single_word[i-1] == 'c' and single_word[i+1] == 'n') or (single_word[i-1] == 'n' and single_word[i+1] == 'c') or (single_word[i-1] == 'c' and single_word[i+1] == 't') or (single_word[i-1] == 't' and single_word[i+1] == 'c')):
						geminate_next_letter = True
						geminated_wordform.append(letter)
				elif word_length-i > 3 and single_word[i+1] in c and single_word[i+2] in v and single_word[i+3] in v:
					geminate_next_letter = True
					geminated_wordform.append(letter)
				else:
					geminated_wordform.append(letter)
			else: # no gemination, normal condition
				geminated_wordform.append(letter)

		### Resolve concatenate syllables
		geminated_wordform = geminated_wordform[::-1] #process in reverse
		word_length = len(geminated_wordform)
		syllable_wordform = []
		last_index = 0
		skip = False
		for i, letter in enumerate(geminated_wordform):
			if skip == True:
				skip = False
			elif word_length-i == 1: # if last character
				syllable_wordform.append(geminated_wordform[last_index:i+1][::-1])
			elif geminated_wordform[i+1] in c:
				syllable_wordform.append(geminated_wordform[last_index:i+2][::-1])
				skip = True
				last_index = i+2
			elif geminated_wordform[i+1] == "'":
				syllable_wordform.append(geminated_wordform[last_index:i+1][::-1])
				syllable_wordform.append("'")
				skip = True
				last_index = i+2
			#If none of these are satisfied then it passes a vowel
		syllable_wordform = syllable_wordform[::-1]

		### handles the apostrophe case first and simultaneously figures out whether
		### voiced fricative by stop or preceding with a voiceless fricative, or s at beginning and r at end, make voiced fric voiceless

		syllable_lookup_format = []
		if syllable_wordform[0] == "'":
			del syllable_wordform[0]
		if syllable_wordform[-1] == "'":
			del syllable_wordform[-1]


		syllable_length = len(syllable_wordform)
		if syllable_wordform[0] != "'" and syllable_wordform[-1] != "'": #just a double check in case there are multiple apostrophes at the ends
			#proceed
			if syllable_wordform[0][0] == 's':
				syllable_wordform[0][0] = voiced_converter['s'] #handle the first and last character s and r cases first
			if syllable_wordform[-1][-1] == 'r':
				syllable_wordform[-1][-1] = voiced_converter['r']		

			if "'" in syllable_wordform: #condition if there is an apostrophe within the word
				double_skip = False
				skip = False
				print(syllable_wordform)
				for i, syllable in enumerate(syllable_wordform):
					if double_skip: #assuming the v ' v condition was called
						double_skip = False
						skip = True
					else:
						if skip:
							skip = False
						else:
							if syllable_length-i == 1: #if last entry
								syllable_lookup_format.append(syllable_wordform[i])
							elif syllable_wordform[i+1] == "'":
								if syllable_wordform[i][-1] in v and syllable_wordform[i+2][0] in v: #if v ' v  then append surrounding syllables
									syllable_lookup_format.append(syllable_wordform[i]+syllable_wordform[i+2])
									double_skip = True
								elif syllable_wordform[i][-1] in c and syllable_wordform[i+2][0] in v: # if c ' v gemination, add the consonant to the right side
									syllable_lookup_format.append(syllable_wordform[i])
									syllable_lookup_format.append(syllable_wordform[i+2].insert(0,syllable_wordform[i][-1]))
									skip = True	
								elif syllable_wordform[i][-1] in c and syllable_wordform[i+2][0] in c:
									syllable_lookup_format.append(syllable_wordform[i])
									skip = True									
								else:
									raise ValueError('this is a rogue apostrophe that doesn\'t follow conventions') 
							else: #if next entry exists and is not an apostrophe, do the fricative analysis
								if (syllable_wordform[i][-1] in voiced_fricatives and syllable_wordform[i+1][0] in stops) or (syllable_wordform[i][-1] in voiced_fricatives and syllable_wordform[i+1][0] in voiceless_fricatives):
									syllable_wordform[i][-1] = voiced_converter[syllable_wordform[i][-1]]
								elif syllable_wordform[i][-1] in stops and syllable_wordform[i+1][0] in voiced_fricatives:
									syllable_wordform[i+1][0] = voiced_converter[syllable_wordform[i+1][0]]
								elif (syllable_wordform[i][-1] in voiced_fricatives and syllable_wordform[i+1][0] in voiced_nasals) or (syllable_wordform[i][-1] in stops and syllable_wordform[i+1][0] in voiced_nasals):
									syllable_wordform[i+1][0] = voiced_converter[syllable_wordform[i+1][0]]
								syllable_lookup_format.append(''.join(syllable_wordform[i]))

			else: #if no apostrophe in the word, doesn't use extra computing to check for apostrophes each loop
				for i, syllable in enumerate(syllable_wordform):
					if syllable_length-i == 1: #if last entry
						syllable_lookup_format.append(''.join(syllable_wordform[i]))
					else:
						if (syllable_wordform[i][-1] in voiced_fricatives and syllable_wordform[i+1][0] in stops) or (syllable_wordform[i][-1] in voiced_fricatives and syllable_wordform[i+1][0] in voiceless_fricatives):
							syllable_wordform[i][-1] = voiced_converter[syllable_wordform[i][-1]]
						elif syllable_wordform[i][-1] in stops and syllable_wordform[i+1][0] in voiced_fricatives:
							syllable_wordform[i+1][0] = voiced_converter[syllable_wordform[i+1][0]]
						elif (syllable_wordform[i][-1] in voiced_fricatives and syllable_wordform[i+1][0] in voiced_nasals) or (syllable_wordform[i][-1] in stops and syllable_wordform[i+1][0] in voiced_nasals):
							syllable_wordform[i+1][0] = voiced_converter[syllable_wordform[i+1][0]]
						syllable_lookup_format.append(''.join(syllable_wordform[i]))
		else:
			raise ValueError('remove additional apostrophe from ends')
		return(syllable_lookup_format)

if __name__ == "__main__":
	s = argparse.ArgumentParser(description='parse a given word into separate units.')
	s.add_argument('file', help='yup\'ik string to be parsed')
	args = s.parse_args()
	print(parser(args.file))

#Tua-i-llu cikuurraarluteng nunaurrluteng. Tamaa-i akmalirnermi, taum cikuliullri, cikum tua-i cikuliurutem tumellritun cikumi teggalqut akmalirnermi uitaut. Cikuupigtellrungatut. Tua-i tauna-llu tuglleq, tugminek ayimciami kuiggaam kangranun, Iqallugtulim-gguq mat’um, tugmi ayimnera elliamiu, waten qanellrunilaraat: “Akwaku kinguliat iliit nalaqekuniu una tugma ayimnera camek kepqutairuciiquq.” Akiuguq tayima. Tuaten taugaam tua-i wiinga qanruteksugngaaqa. Taugaam man’a maani tua-i mer’ullrunilaryaaqaat nunaurpailgan. Wiinga qanemciuluku niitellemni qamkut qama-i Kalskag-armiut ingrit nuukait. Ukuk wani Kuigpiinkuk Kusquqviim-llu akiqliin ingrikenka akuliitni Kalskag-armiut; tua-i uatiit man’ ingritailnguq. Niitellruunga taum-gguq Ciuliaqatuum qamllerkuani ciqruskii qanerluni, “Akwaku kinguliat nunakniaraat.” Tua-i-gguq nunaurtellruuq maa-i man’a taum qamllerkuaminek ciqrucillra ayagneqluku. Tuaten wii qanemciuluku nallunritetaaqa. Qukailnguq: Ukut cali waniwa wii niitelallemni qanemciuluki tamaa-i evunrullruniluki qanrutkelallruit qanrutkestiita. Evunrullruut-gguq ukut ingrit.
#Tauna-am pania uingvailegmi qingalliniuq, qingarnariani-w’ tua-i pillilria. Tua-i apqiitnek atailngiluni; nallunailngurmek atalguvkenani. Tua-i-am taum apaurluan yuurcan tua-i umyuamikun cakneq cingumiimiu waten ataunani yuurtellra pitekluku, apaurluan taum tayima anguyalangneratgun pillian. Imkut yaqulget qucillgarnek aptukait, erinvaulalriit, yaaqsing’ermeng-llu qalriagaqameng alaitaqluteng. Tamakucirtaqami apaurluan taum qucillgarmek, tekitaqami nuliaminun man’a qakerlua qalriassuutii augaasqelallinia. Tua-i-llu nuliaminun aug’arceqaarluku aug’aqaku apaurluan taum teguluku mikelnguyagaullrani tauna Apanuugpak, maavet qalriassutii qucillgam minguutelallinia, qanerluni, “Anguyagyaureskan anguyain eriniikun alikelarniaraat.” Cunawa-gguq tua-i-am nall’arulluni; anguyalangan eriniikun anguyain alikaqluku. Apaurluan-am tua-i tauna cingumatii nall’arusngaluni, erinvauluni Apanuugpak tauna pillrulliniuq.