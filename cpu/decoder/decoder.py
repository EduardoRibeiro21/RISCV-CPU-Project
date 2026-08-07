class Decoder:
    def get_opcode(self, bits):
        return bits & 0x7F

    def extract_Rtype(self, bits):
        instruction = {
            "opcode": self.get_opcode(bits),
            "rd": (bits >> 7) & 0x1F,
            "funct3": (bits >> 12) & 0x07,
            "rs1": (bits >> 15) & 0x1F,
            "rs2": (bits >> 20) & 0x1F,
            "funct7": (bits >> 25) & 0x7F
        }

        return instruction

    def extract_Itype(self, bits):
            instruction = {
                "opcode": self.get_opcode(bits),
                "rd": (bits >> 7) & 0x1F,
                "funct3": (bits >> 12) & 0x07,
                "rs1": (bits >> 15) & 0x1F,
                "imm": (bits >> 20) & 0xFFF
            }
    
            return instruction

    def extract_Stype(self, bits):
            instruction = {
                "opcode": self.get_opcode(bits),
                "rd": (bits >> 7) & 0x1F,
                "imm_1": (bits >> 12) & 0x07,
                "rs1": (bits >> 15) & 0x1F,
                "rs2": (bits >> 20) & 0x1F,
                "imm_2": (bits >> 25) & 0x7F
            }

            instruction["imm"] = (instruction["imm_1"] << 5) & instruction["imm_2"]
    
            return instruction

    """TODO: implementing the others extractions"""
    def extract_Rtype(self, bits):
            instruction = {
                "opcode": self.get_opcode(bits),
                "rd": (bits >> 7) & 0x1F,
                "funct3": (bits >> 12) & 0x07,
                "rs1": (bits >> 15) & 0x1F,
                "rs2": (bits >> 20) & 0x1F,
                "funct7": (bits >> 25) & 0x7F
            }
    
            return instruction

    def extract_Rtype(self, bits):
            instruction = {
                "opcode": self.get_opcode(bits),
                "rd": (bits >> 7) & 0x1F,
                "funct3": (bits >> 12) & 0x07,
                "rs1": (bits >> 15) & 0x1F,
                "rs2": (bits >> 20) & 0x1F,
                "funct7": (bits >> 25) & 0x7F
            }
    
            return instruction

    def extract_Rtype(self, bits):
            instruction = {
                "opcode": self.get_opcode(bits),
                "rd": (bits >> 7) & 0x1F,
                "funct3": (bits >> 12) & 0x07,
                "rs1": (bits >> 15) & 0x1F,
                "rs2": (bits >> 20) & 0x1F,
                "funct7": (bits >> 25) & 0x7F
            }
    
            return instruction




# 0b00000000010100101010100000100011

# 1111111
# 1111 1000 0000 0000 0000
# 1110