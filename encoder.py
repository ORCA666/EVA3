#!/usr/bin/python
#coded by orca666

import sys


# Your shellcode [x64 https]
raw_data = "ur shellcode"

encoded_shellcode = []
for opcode in raw_data:
  
        new_opcode = (ord(opcode) ^ 0x69)
        encoded_shellcode.append(new_opcode)
print("".join(["\\x{0}".format(hex(abs(i)).replace("0x", "")) for i in encoded_shellcode]))
