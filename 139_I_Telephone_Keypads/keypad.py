# Daily programer challenge 139 - Telephone Keypads - Intermediate
# http://www.reddit.com/r/dailyprogrammer/comments/1sody4/12113_challenge_139_intermediate_telephone_keypads/

import re, sys

numMap = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz",
}

nums = [val[0] for val in sys.argv[1:]] # Doing Challenge++, discard frequency info

words = open('/usr/share/dict/words').read().lower().rstrip()
charsList = []
for num in nums:
	try:
		charsList.append(numMap[num])
	except KeyError:
		pass # ignore 0s and 1s

# Build-up regex pattern
pattern = ""
for charset in charsList:
	pattern += "[%s]" % charset
pattern += "\w*"

# Retrieve unique matches
matches = set(re.findall(pattern, words))
print sorted(matches, key=len)