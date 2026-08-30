from cpu.alu.alu import ALU
from cpu.control.control_unit import ControlUnit
from cpu.control.alu_control import ALUControl
from cpu.decoder.decoder import Decoder
from cpu.datapath.register_file import RegisterFile

class Datapath:
    def __init__(self, memory, register_file):
        # Estado principal
        self.PC = 0x00400000
        self.memory = memory
        self.register_file = register_file

        # Componentes
        self.decoder = Decoder()
        self.control_unit = ControlUnit()
        self.alu_control = ALUControl()
        self.alu = ALU()
        self.register = RegisterFile()

    # --- Fases do ciclo ---

    def fetch(self):
        """Busca a instrução da memória usando o PC."""
        

    def decode(self, instr):
        """Extrai campos da instrução usando o decoder."""
        pass

    def generate_control_signals(self, fields):
        """Gera sinais de controlo a partir do opcode."""
        pass

    def read_registers(self):
        """Lê rs1 e rs2 do Register File."""
        return self.register.read()

    def select_alu_operands(self, signals, fields, op1, op2):
        """Escolhe entre rs2 ou imediato (MUX ALUSrc)."""
        pass

    def execute_alu(self, op1, op2, signals, fields):
        """Executa a operação na ALU."""
        pass

    def memory_access(self, signals, alu_result, op2):
        """Executa lw ou sw se necessário."""
        pass

    def write_back(self, signals, fields, alu_result, mem_value):
        """Escreve no registo destino (MUX MemToReg)."""
        pass

    def update_pc(self, signals, fields, alu_result):
        """Atualiza o PC (PC+4, branch, jump)."""
        pass

    def step(self):
        """Executa um ciclo completo do CPU."""
        pass
