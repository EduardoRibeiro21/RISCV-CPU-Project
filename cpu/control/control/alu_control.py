class ALUControl:
    def decode(self, ALUOp, funct3, funct7):
        if ALUOp == 0:
            return "ADD"   # ADDI, LW, SW

        if ALUOp == 1:
            return "SUB"   # BEQ

        if ALUOp == 2:     # R-type
            if funct3 == 0 and funct7 == 0:
                return "ADD"
            if funct3 == 0 and funct7 == 0x20:
                return "SUB"
            if funct3 == 7:
                return "AND"
            if funct3 == 6:
                return "OR"
            if funct3 == 4:
                return "XOR"

        if ALUOp == 3:     # LUI
            return "LUI"

        raise ValueError("Unknown ALU operation")