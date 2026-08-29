from cpu.decoder.decoder import Decoder

decoder = Decoder()

"""R-type decodification tests"""
Rtype_bit = 0b00000000011100110000001010110011
Rtype_instr = decoder.extract_Rtype(Rtype_bit)

assert Rtype_instr["rd"] == 5
assert Rtype_instr["rs1"] == 6
assert Rtype_instr["rs2"] == 7
assert Rtype_instr["funct3"] == 0
assert Rtype_instr["funct7"] == 0
assert Rtype_instr["opcode"] == 0x33


"""I-type decodification tests"""
Itype_bit = 0b111111101100010000000010010011
Itype_instr = decoder.extract_Itype(Itype_bit)

assert Itype_instr["rd"] == 1
assert Itype_instr["rs1"] == 2
assert Itype_instr["funct3"] == 0
assert Itype_instr["imm"] == 0x3FB
assert Itype_instr["opcode"] == 0x13


"""S-type decodification tests"""
Stype_bit = 0b11111110011101000010011000100011
Stype_instr = decoder.extract_Stype(Stype_bit)

assert Stype_instr["rs1"] == 8
assert Stype_instr["rs2"] == 7
assert Stype_instr["funct3"] == 2
assert Stype_instr["imm"] == -20
assert Stype_instr["opcode"] == 0x23


"""B-type decodification tests"""
Btype_bit = 0b11111100001000001000111001100011
Btype_instr = decoder.extract_Btype(Btype_bit)

assert Btype_instr["rs1"] == 1
assert Btype_instr["rs2"] == 2
assert Btype_instr["funct3"] == 0
assert Btype_instr["imm"] == -2084
assert Btype_instr["opcode"] == 0x63


"""U-type decodification tests"""
Utype_bit = 0b00010010001101000101000110110111
Utype_instr = decoder.extract_Utype(Utype_bit)

assert Utype_instr["rd"] == 3
assert Utype_instr["imm"] == 0x12345
assert Utype_instr["opcode"] == 0x37


"""J-type decodification tests"""
Jtype_bit = 0b1111111010111111111000011101111
Jtype_instr = decoder.extract_Jtype(Jtype_bit)

assert Jtype_instr["rd"] == 1
assert Jtype_instr["imm"] == 1048564
assert Jtype_instr["opcode"] == 0x6F


print("Decoder tests passed!")