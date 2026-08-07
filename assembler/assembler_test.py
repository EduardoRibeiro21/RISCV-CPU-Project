def test_assembler():
    with open("riscv_code.txt", "w") as riscv_code:
        
        instructions = [
            "sw x5, 16(x5)",    # Instruction 1
            "lw x6, 16(x5)",    # Instruction 2
            "add x7, x6, x0",   # Instruction 3
            "sub x28, x0, x28", # Instruction 4
            "and x5, x5, x29",  # Instruction 5
            "or x20, x30, x31"  # Instruction 6
        ]
        
        riscv_code.writelines('\n'.join(instructions))

    #assemble()

    lines_bin = []
    with open("machine_code.txt", "r") as machine_code:
        for line in machine_code:
            lines_bin.append(line.strip())

    expected = [
            "00000000010100101010100000100011", # Expected 1
            "00000001000000101010001100000011", # Expected 2
            "00000000000000110000001110110011", # Expected 3
            "01000001110000000000111000110011", # Expected 4
            "00000001110100101111001010110011", # Expected 5
            "00000001111111110110101000110011"  # Expected 6
        ]

    if len(lines_bin) != len(expected):
        print(f"Expected {len(expected)} lines, got {len(lines_bin)}.")
    
    else:
        for i, (actual, exp) in enumerate(zip(lines_bin, expected)):
            try:
                assert actual == exp
            except AssertionError:
                print(f"Instruction {i+1} failed.")
                print(f"Expected: {exp}")
                print(f"Got:      {actual}")
                return
            else:
                print(f"Instruction {i+1} OK.")
    
    print("All instructions OK!")
    
test_assembler()