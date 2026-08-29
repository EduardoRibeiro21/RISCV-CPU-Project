from cpu.alu.alu import ALU

alu = ALU()

assert alu.execute(5, 3, "ADD") == 8
assert alu.execute(5, 3, "SUB") == 2
assert alu.execute(0b1100, 0b1010, "AND") == 0b1000
assert alu.execute(0b1100, 0b1010, "OR") == 0b1110
assert alu.execute(0b1100, 0b1100, "XOR") == 0b0000
assert alu.execute(0b0111, 0b0001, "SLL") == 0b1110
assert alu.execute(0b1110, 0b0001, "SRL") == 0b0111
assert alu.execute(0b1100, 0b1010, "SLT") == 0
assert alu.execute(0b1010, 0b1100, "SLT") == 1

print("ALU tests passed!")