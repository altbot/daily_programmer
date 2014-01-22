import re, sys

def sub(s):
    """ Substitute operand mnemonics for regexes """
    s = s.replace('s', r"\s+") # whitespace
    s = s.replace('l', r"(\w+)") # literal args
    s = s.replace('m', r"(\[\w+\])") # memory args
    return s

ops = {
    # Logic ops
    r'AND'  + sub('smsm'): '0x00',
    r'AND'  + sub('smsl'): '0x01',
    r'OR'   + sub('smsm'): '0x02',
    r'OR'   + sub('smsl'): '0x03',
    r'XOR'  + sub('smsm'): '0x04',
    r'XOR'  + sub('smsl'): '0x05',
    r'NOT'  + sub('sm'):   '0x06',

    # Memory ops
    r'MOV'  + sub('smsm'): '0x07',
    r'MOV'  + sub('smsl'): '0x08',

    # Math ops
    r'RANDOM' + sub('sl'): '0x09',
    r'ADD'  + sub('smsm'): '0x0a',
    r'ADD'  + sub('smsl'): '0x0b',
    r'SUB'  + sub('smsm'): '0x0c',
    r'SUB'  + sub('smsl'): '0x0d',

    # Control ops
    r'JMP'  + sub('sm'): '0x0e',
    r'JMP'  + sub('sl'): '0x0f',
    r'JZ'   + sub('smsm'): '0x10',
    r'JZ'   + sub('smsl'): '0x11',
    r'JZ'   + sub('slsm'): '0x12',
    r'JZ'   + sub('slsl'): '0x13',
    r'JEQ'  + sub('smsmsm'): '0x14',
    r'JEQ'  + sub('slsmsm'): '0x15',
    r'JEQ'  + sub('smsmsl'): '0x16',
    r'JEQ'  + sub('slsmsl'): '0x17',
    r'JLS'  + sub('smsmsm'): '0x18',
    r'JLS'  + sub('slsmsm'): '0x19',
    r'JLS'  + sub('smsmsl'): '0x1a',
    r'JLS'  + sub('slsmsl'): '0x1b',
    r'JGT'  + sub('smsmsm'): '0x1c',
    r'JGT'  + sub('slsmsm'): '0x1d',
    r'JGT'  + sub('smsmsl'): '0x1e',
    r'JGT'  + sub('slsmsl'): '0x1f',
    r'HALT': '0xff',

    # Utilities
    r'DPRINT' + sub('sm'): '0x20',
    r'DPRINT' + sub('sl'): '0x21',
    r'DPRINT' + sub('sm'): '0x22',
    r'DPRINT' + sub('sl'): '0x23',
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
            # Try and get up to three match groups - arg arg arg
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
