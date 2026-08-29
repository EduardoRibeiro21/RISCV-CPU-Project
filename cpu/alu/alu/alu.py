class ALU:
    def execute(self, op1, op2, alu_op):
        if alu_op == "ADD":
            return op1 + op2

        elif alu_op == "SUB":
            return op1 - op2

        elif alu_op == "AND":
            return op1 & op2

        elif alu_op == "OR":
            return op1 | op2

        elif alu_op == "XOR":
            return op1 ^ op2

        elif alu_op == "SLL":
            return op1 << (op2 & 0x1F)

        elif alu_op == "SRL":
            return op1 >> (op2 & 0x1F)

        elif alu_op == "SLT":
            return 1 if op1 < op2 else 0

        else:
            raise ValueError(f"Unknown ALU operation: {alu_op}")