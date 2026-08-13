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
        imm = (bits >> 20) & 0xFFF

        if imm & (1 << 11):
            imm -= (1 << 12)

        instruction = {
            "opcode": self.get_opcode(bits),
            "rd": (bits >> 7) & 0x1F,
            "funct3": (bits >> 12) & 0x07,
            "rs1": (bits >> 15) & 0x1F,
            "imm": imm
        }

        return instruction

    def extract_Stype(self, bits):
        imm_1 = (bits >> 7) & 0x1F
        imm_2 = (bits >> 25) & 0x7F

        imm = (imm_2 << 5) | imm_1

        if imm & (1 << 11):
            imm -= (1 << 12)

        instruction = {
            "opcode": self.get_opcode(bits),
            "funct3": (bits >> 12) & 0x07,
            "rs1": (bits >> 15) & 0x1F,
            "rs2": (bits >> 20) & 0x1F,
            "imm": imm
        }

        return instruction

    def extract_Btype(self, bits):
        imm_1 = (bits >> 8) & 0x0F
        imm_2 = (bits >> 25) & 0x3F
        imm_3 = (bits >> 7) & 0x01
        imm_4 = (bits >> 31) & 0x01

        imm = (imm_4 << 12) | (imm_3 << 11) | (imm_2 << 5) | (imm_1 << 1)

        if imm & (1 << 12):
            imm -= (1 << 13)

        instruction = {
            "opcode": self.get_opcode(bits),
            "funct3": (bits >> 12) & 0x07,
            "rs1": (bits >> 15) & 0x1F,
            "rs2": (bits >> 20) & 0x1F,
            "imm": imm
        }

        return instruction

    def extract_Utype(self, bits):
        imm = (bits >> 12) & 0xFFFFF

        if imm & (1 << 19):
            imm -= (1 << 20)

        instruction = {
            "opcode": self.get_opcode(bits),
            "rd": (bits >> 7) & 0x1F,
            "imm": imm
        }

        return instruction

    def extract_Jtype(self, bits):
        imm_1 = (bits >> 21) & 0x3FF
        imm_2 = (bits >> 20) & 0x01
        imm_3 = (bits >> 12) & 0xFF
        imm_4 = (bits >> 31) & 0x01

        imm = (imm_4 << 20) | (imm_3 << 12) | (imm_2 << 11) | (imm_1 << 1)

        if imm & (1 << 20):
            imm -= (1 << 21)

        instruction = {
            "opcode": self.get_opcode(bits),
            "rd": (bits >> 7) & 0x1F,
            "imm": imm
        }

        return instruction

# 0b00000000010100101010100000100011

# 1111111
# 1111 1000 0000 0000 0000
# 1110