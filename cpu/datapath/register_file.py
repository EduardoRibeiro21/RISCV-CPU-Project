class RegisterFile:
    def __init__(self, initial_values=None):
        # Se initial_values for None, cria 32 registos a zero
        # Caso contrário, usa a lista que forneceste
        self.regs = initial_values if initial_values else [0] * 32

    def read(self, rs1, rs2):
        """Lê os registos rs1 e rs2."""
        pass

    def write(self, rd, value, reg_write):
        """Escreve no registo rd se reg_write == 1 e rd != 0."""
        pass

    def dump(self):
        """Opcional: imprime todos os registos para debugging."""
        pass

    def reset(self, initial_values):
        """Opcional: recarrega os valores iniciais."""
        pass
