import re, sys

m = r"(\[\w+\])"    # memory
l = r"\w+"          # literal
sp = r"\s+"         # space

# Build Regexes for matching args
sm = sp + m
sl = sp + l
mm = sm + sm # double memory
ml = sm + sl # memory, literal
lm = sl + sm # literal, memory
ll = sl + sl # literal, literal
mmm = mm + sm
lml = sl + sm + sl
lmm = sl + mm
mll = sm + ll
mml = mm + sl
lml = sl + sm + sl

ops = {
    # Logic ops
    r'AND'  + mm: '0x00',
    r'AND'  + ml: '0x01',
    r'OR'   + mm: '0x02',
    r'OR'   + ml: '0x03',
    r'XOR'  + mm: '0x04',
    r'XOR'  + ml: '0x05',
    r'NOT'  + m:  '0x06',

    # Memory ops
    r'MOV'  + mm: '0x07',
    r'MOV'  + ml: '0x08',

    # Math ops
    r'RANDOM' + sl: '0x09',
    r'ADD'  + mm: '0x0a',
    r'ADD'  + ml: '0x0b',
    r'SUB'  + mm: '0x0c',
    r'SUB'  + ml: '0x0d',

    # Control ops
    r'JMP'  + m: '0x0e',
    r'JMP'  + l: '0x0f',
    r'JZ'   + mm: '0x10',
    r'JZ'   + ml: '0x11',
    r'JZ'   + lm: '0x12',
    r'JZ'   + ll: '0x13',
    r'JEQ'  + mmm: '0x14',
    r'JEQ'  + lmm: '0x15',
    r'JEQ'  + mml: '0x16',
    r'JEQ'  + lml: '0x17',
    r'JLS'  + mmm: '0x18',
    r'JLS'  + lmm: '0x19',
    r'JLS'  + mml: '0x1a',
    r'JLS'  + lml: '0x1b',
    r'JGT'  + mmm: '0x1c',
    r'JGT'  + lmm: '0x1d',
    r'JGT'  + mml: '0x1e',
    r'JGT'  + lml: '0x1f',
    r'HALT': '0xff',

    # Utilities
    r'DPRINT' + m: '0x20',
    r'DPRINT' + l: '0x21',
    r'DPRINT' + m: '0x22',
    r'DPRINT' + l: '0x23',
}

try:
    inFile = sys.argv[1]
except IndexError:
    inFile = "input.txt"
try:
    desiredOutput = sys.argv[2]
except IndexError:
    testFile = "output.txt"

source = [line.strip() for line in open(inFile).readlines()]
desiredOutput = [line.strip() for line in open(testFile).readlines()]
output = []

for line in source:
    #print line
    for mnemonic in ops.keys():
        match = re.match(mnemonic, line, flags=re.I)
        if match:
            opcode = ops[mnemonic]
            # Try and get up to three match groups - arg arg
            for i in xrange(1, 4):
                try:
                    arg = (match.group(i))
                    if arg[0] == "[" and arg[-1] == "]":
                        #do some memory reading shiz
                        arg = arg[1:-1]
                    opcode += " 0x%0.2X" % int(arg)
                except IndexError:
                    break
                output.append(opcode)
            break

print output
print desiredOutput
