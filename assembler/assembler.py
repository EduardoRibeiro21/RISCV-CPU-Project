with open("riscv_code.txt", "w") as riscv_code:
    instructions = []
    instr = input().strip()
    
    while instr:
        instructions.append(instr)
        instr = input()
    
    riscv_code.write("\n".join(instructions))


def assemble():
    with open("riscv_code.txt", "r") as riscv_code, open("machine_code.txt", "w") as machine_code:
        pass # do not include this
    
        # TODO: writing some code here
        
    pc = 0x00400000
    return pc
