# Daily Programmer Challenge 143 - Braille - Easy
# http://www.reddit.com/r/dailyprogrammer/comments/1s061q/120313_challenge_143_easy_braille/

# Optimisation - divide {a-j}, {k-t}, {u,v,x,y,z}, {w} into their own
# dicts and use common characteristics to determine which dict to lookup
brailleMap = {
('O.', 'OO', 'OO'): 'a',
('O.', 'O.', '..'): 'b',
('OO', '..', '..'): 'c',
('OO', '.O', '..'): 'd',
('O.', '.O', '..'): 'e',
('OO', 'O.', '..'): 'f',
('OO', 'OO', '..'): 'g',
('O.', 'OO', '..'): 'h',
('.O', 'O.', '..'): 'i',
('.O', 'OO', '..'): 'j',
('O.', '..', 'O.'): 'k',
('O.', 'O.', 'O.'): 'l',
('OO', '..', 'O.'): 'm',
('OO', '.O', 'O.'): 'n',
('O.', '.O', 'O.'): 'o',
('OO', 'O.', 'O.'): 'p',
('OO', 'OO', 'O.'): 'q',
('O.', 'OO', 'O.'): 'r',
('.O', 'O.', 'O.'): 's',
('.O', 'OO', 'O.'): 't',
('O.', '..', 'OO'): 'u',
('O.', 'O.', 'OO'): 'v',
('.O', 'OO', '.O'): 'w',
('OO', '..', 'OO'): 'x',
('OO', '.O', 'OO'): 'y',
('O.', '.O', 'OO'): 'z',
}

lines = [line.rstrip().split() for line in open('input.txt')]

letters = []
for i in xrange(len(lines[0])):
	letters.extend(zip(lines[0][i:i+1], lines[1][i:i+1], lines[2][i:i+1] ))

translation = ''
for letter in letters:
	translation += brailleMap[letter]

desiredOutput = open('output.txt').read().strip()
if translation == desiredOutput:
	print translation
else:
	print "Failure, translation does not match desired output"
	print "translation:", translation
	print "desired output", desiredOutput
