# Daily programer challenge 132 - Tiny Assembly - Intermediate
# http://www.reddit.com/r/dailyprogrammer/comments/1kqxz9/080813_challenge_132_intermediate_tiny_assembler/

import re, sys

def sub(asm):
    """ Substitute operand mnemonics for regexes """
    asm = asm.replace('s', r"\s+") # whitespace
    asm = asm.replace('l', r"(\w+)") # literal args
    asm = asm.replace('m', r"(\[\w+\])") # memory args
    return asm

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
    r'ADD'  + sub('smsm'): '0x0A',
    r'ADD'  + sub('smsl'): '0x0B',
    r'SUB'  + sub('smsm'): '0x0C',
    r'SUB'  + sub('smsl'): '0x0D',

    # Control ops
    r'JMP'  + sub('sm'): '0x0E',
    r'JMP'  + sub('sl'): '0x0F',
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
    r'JLS'  + sub('smsmsl'): '0x1A',
    r'JLS'  + sub('slsmsl'): '0x1B',
    r'JGT'  + sub('smsmsm'): '0x1C',
    r'JGT'  + sub('slsmsm'): '0x1D',
    r'JGT'  + sub('smsmsl'): '0x1E',
    r'JGT'  + sub('slsmsl'): '0x1F',
    r'HALT': '0xFF',

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

source = [line.strip() for line in open(inFile).readlines()]

output = []
for line in source:
    # Iterating through dict might not be best in terms of efficiency
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
