from math import log10
from math import tanh

# Aeronautics Constants
rho = 0.00238


# Rivets
class Rivet:
    def __init__(self, designation: str, diameter: float, ult_shear: int):
        self.designation: str = designation
        self.diameter: float = diameter
        self.ult_shear: int = ult_shear


class Tail:
    def __init__(self):
        pass


class Fuselage:
    def __init__(self):
        pass


def kuhn_diagonal_factor(tao, tao_cr):
    return tanh(0.5 * log10(tao / tao_cr))
