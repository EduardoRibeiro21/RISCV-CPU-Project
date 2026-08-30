from cpu.decoder.decoder import Decoder

decoder = Decoder()

with open("riscv_code.txt", "w") as riscv_code:
    instructions = []
    instr = input().strip()
    
    while instr:
        instructions.append(instr)
        instr = input()
    
    riscv_code.write("\n".join(instructions))


def assemble():
    with open("riscv_code.txt", "r") as riscv_code, open("machine_code.txt", "w") as machine_code:
        for line in riscv_code:
            keyword = ""
            for char in line:
                if char == " ":
                    break
                keyword += char

            
    
        # TODO: writing some code here
        
    pc = 0x00400000
    return pc
