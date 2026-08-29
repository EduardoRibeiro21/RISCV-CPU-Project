import pytest
from cpu.control.control_unit import ControlUnit
from cpu.control.alu_control import ALUControl

cu = ControlUnit()
alu_ctrl = ALUControl()


"""Control unit tests"""

def test_Rtype_control():
    signals = cu.decode(0x33)
    assert signals["RegWrite"] == 1
    assert signals["ALUSrc"]   == 0
    assert signals["MemRead"]  == 0
    assert signals["MemWrite"] == 0
    assert signals["Branch"]   == 0
    assert signals["Jump"]     == 0
    assert signals["MemToReg"] == 0
    assert signals["ALUOp"]    == 2


def test_Itype_control():
    signals = cu.decode(0x13)
    assert signals["RegWrite"] == 1
    assert signals["ALUSrc"]   == 1
    assert signals["MemRead"]  == 0
    assert signals["MemWrite"] == 0
    assert signals["Branch"]   == 0
    assert signals["Jump"]     == 0
    assert signals["MemToReg"] == 0
    assert signals["ALUOp"]    == 0


def test_Stype_control():
    signals = cu.decode(0x23)
    assert signals["RegWrite"] == 0
    assert signals["ALUSrc"]   == 1
    assert signals["MemRead"]  == 0
    assert signals["MemWrite"] == 1
    assert signals["Branch"]   == 0
    assert signals["Jump"]     == 0
    assert signals["ALUOp"]    == 0


def test_Btype_control():
    signals = cu.decode(0x63)
    assert signals["RegWrite"] == 0
    assert signals["ALUSrc"]   == 0
    assert signals["MemRead"]  == 0
    assert signals["MemWrite"] == 0
    assert signals["Branch"]   == 1
    assert signals["Jump"]     == 0
    assert signals["ALUOp"]    == 1


def test_Utype_control():
    signals = cu.decode(0x37)
    assert signals["RegWrite"] == 1
    assert signals["ALUSrc"]   == 1
    assert signals["MemRead"]  == 0
    assert signals["MemWrite"] == 0
    assert signals["Branch"]   == 0
    assert signals["Jump"]     == 0
    assert signals["MemToReg"] == 0
    assert signals["ALUOp"]    == 3


def test_Jtype_control():
    signals = cu.decode(0x6F)
    assert signals["RegWrite"] == 1
    assert signals["Jump"]     == 1
    assert signals["Branch"]   == 0
    assert signals["MemRead"]  == 0
    assert signals["MemWrite"] == 0
    assert signals["MemToReg"] == 2


"""ALU Control tests"""

def test_ALUControl_add():
    op = alu_ctrl.decode(ALUOp=2, funct3=0, funct7=0)
    assert op == "ADD"

def test_ALUControl_sub():
    op = alu_ctrl.decode(ALUOp=2, funct3=0, funct7=0x20)
    assert op == "SUB"

def test_ALUControl_and():
    op = alu_ctrl.decode(ALUOp=2, funct3=7, funct7=0)
    assert op == "AND"

def test_ALUControl_or():
    op = alu_ctrl.decode(ALUOp=2, funct3=6, funct7=0)
    assert op == "OR"

def test_ALUControl_xor():
    op = alu_ctrl.decode(ALUOp=2, funct3=4, funct7=0)
    assert op == "XOR"


"""Invalid cases"""

def test_unknown_opcode():
    assert cu.decode(0x00) is None

def test_invalid_alu_control():
    with pytest.raises(ValueError):
        alu_ctrl.decode(ALUOp=2, funct3=3, funct7=0)


print("Control tests passed!")