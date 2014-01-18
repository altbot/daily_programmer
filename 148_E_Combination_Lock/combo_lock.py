# Daily Programmer Challenge 148 - Combination Lock - Easy
# http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/

import sys
numDigits = int(sys.argv[1])
code = [int(val) for val in sys.argv[2:5]]

# Steps:
# spin two rotations clockwise
# spin to first number of code
# spin one rotation counter-clockwise
# spin to second number counter-clockwise
# spin from second to third number clockwise

print numDigits * 4 + code[0] * 2  + code[2] - code[1] * 2
