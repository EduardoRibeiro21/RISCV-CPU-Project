class ControlUnit:
    def __init__(self):
        self.control_map = {
            0x33: {  # R-type
                "RegWrite": 1, "ALUSrc": 0, "MemRead": 0, "MemWrite": 0,
                "Branch": 0, "Jump": 0, "MemToReg": 0, "ALUOp": 2
            },
            0x13: {  # I-type (ADDI)
                "RegWrite": 1, "ALUSrc": 1, "MemRead": 0, "MemWrite": 0,
                "Branch": 0, "Jump": 0, "MemToReg": 0, "ALUOp": 0
            },
            0x23: {  # S-type (SW)
                "RegWrite": 0, "ALUSrc": 1, "MemRead": 0, "MemWrite": 1,
                "Branch": 0, "Jump": 0, "MemToReg": None, "ALUOp": 0
            },
            0x63: {  # B-type (BEQ)
                "RegWrite": 0, "ALUSrc": 0, "MemRead": 0, "MemWrite": 0,
                "Branch": 1, "Jump": 0, "MemToReg": None, "ALUOp": 1
            },
            0x37: {  # U-type (LUI)
                "RegWrite": 1, "ALUSrc": 1, "MemRead": 0, "MemWrite": 0,
                "Branch": 0, "Jump": 0, "MemToReg": 0, "ALUOp": 3
            },
            0x6F: {  # J-type (JAL)
                "RegWrite": 1, "ALUSrc": None, "MemRead": 0, "MemWrite": 0,
                "Branch": 0, "Jump": 1, "MemToReg": 2, "ALUOp": None
            }
        }

    def decode(self, opcode):
        return self.control_map.get(opcode, None)
