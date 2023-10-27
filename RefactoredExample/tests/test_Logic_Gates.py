import sys
sys.path.append("./RefactoredExample/src/")
from main import LogicGate, BinaryGate, ANDGate, ORGate, XORGate, UnaryGate, NOTGate, NANDGate, NORGate, Connector


def test_LogicGate():
    lg = LogicGate("LG")
    assert lg.get_label() == "LG"


def test_BinaryGate():
    bg = BinaryGate("BG")
    bg.set_a(1)
    bg.set_b(0)
    assert bg.get_pin_a() == 1
    assert bg.get_pin_b() == 0


def test_ANDGate():
    and_gate = ANDGate("AND")
    and_gate.set_a(1)
    and_gate.set_b(0)
    assert and_gate.perform_gate_logic() == 0


def test_ORGate():
    or_gate = ORGate("OR")
    or_gate.set_a(1)
    or_gate.set_b(0)
    assert or_gate.perform_gate_logic() == 1


def test_XORGate():
    xor_gate = XORGate("XOR")
    xor_gate.set_a(1)
    xor_gate.set_b(0)
    assert xor_gate.perform_gate_logic() == 1


def test_UnaryGate():
    ug = UnaryGate("UG")
    ug.set_next_pin(1)
    assert ug.get_pin() == 1


def test_NOTGate():
    not_gate = NOTGate("NOT")
    not_gate.set_next_pin(1)
    assert not_gate.perform_gate_logic() == 0


def test_NANDGate():
    nand_gate = NANDGate("NAND")
    nand_gate.set_a(1)
    nand_gate.set_b(0)
    assert nand_gate.perform_gate_logic() == 1


def test_NORGate():
    nor_gate = NORGate("NOR")
    nor_gate.set_a(1)
    nor_gate.set_b(0)
    assert nor_gate.perform_gate_logic() == 0


def test_Connector():
    lg1 = LogicGate("LG1")
    lg2 = LogicGate("LG2")
    connector = Connector(lg1, lg2)
    assert connector.get_from().get_label() == "LG1"
    assert connector.get_to().get_label() == "LG2"
