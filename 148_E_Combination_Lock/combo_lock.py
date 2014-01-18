# Daily Programmer Challenge 148 - Combination Lock - Easy
# http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/

import sys
numDigits = int(sys.argv[1])
code = [int(val) for val in sys.argv[2:5]]
numIncrements = numDigits * 2 # spin two rotations clockwise
numIncrements += code[0] # spin to first number of code
numIncrements += numDigits # spin one rotation counter-clockwise
numIncrements += code[0] + numDigits - code[1] # spin to second number counter-clockwise
numIncrements += code[2] - code[1] # spin from second to third number clockwise
print numIncrements