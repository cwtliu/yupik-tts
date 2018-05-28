"""
Spellcheck for Yup'ik words. Looks for English letters, illegal characters & combinations. Does not make spelling
corrections
"""

#__author__ = "Baxter Bond"
#__version__ = "0.0.0"

import re


def spellcheck(word):  #returns true when all spell checks have passed, otherwise returns false
    word = word.lower()  #sterilize capitilizations
    if re.search(r"[^-'acegiklmnpqrstuvwy]", word):  #illegal letters or special characters not use
        print("English letter or illegal symbol error")
        return False
    elif re.search(r"[aui]{3,}|[auie]e|e[eaui]", word): #triple vowels or vowels with e
        print("Triple vowels or improper vowel error")
        return False
    elif re.search(r"([glrsv])\1\1|([ckmnpqtwy])\2", word): #two or more non-fricatives or 3 or more fricatives
        print("consonant combination error")
        return False
    elif re.search(r"[ckpqt]'*([glrsv])\1|([glrsv])\2'*[ckpqt]", word): #stop followed/preceded by two or more fricatves
        print("stop devoicing error")
        return False
    elif re.search(r"([glrsv])\1([glrsv])\2", word):
        print("fricative devoicing error")
        return False
    elif re.search(r"[cgklmnpqrstvwy]{3,}", word):
        print("triple consonant error")
        return False
    else:
        return True

#print(spellcheck("ayagg'tuq"))
