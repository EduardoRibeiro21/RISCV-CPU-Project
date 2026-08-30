class RegisterFile:
    def __init__(self, initial_values=None):
        # Se initial_values for None, cria 32 registos a zero
        # Caso contrário, usa a lista que forneceste
        self.regs = initial_values if initial_values else [0] * 32

    def read(self, rs1, rs2):
        """Lê os registos rs1 e rs2."""
        return self.regs[rs1], self.regs[rs2]

    def write(self, rd, value, reg_write):
        """Escreve no registo rd se reg_write == 1 e rd != 0."""
        if reg_write == 1 and rd != 0:
            self.regs[rd] = value

    def dump(self):
        """Opcional: imprime todos os registos para debugging."""
        for i, val in enumerate(self.regs):
            print(f"x{i:02} = 0x{val:08x}")

    def reset(self, initial_values):
        """Opcional: recarrega os valores iniciais."""
        self.regs = initial_values.copy()
