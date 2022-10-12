import math


class Metal:
    def __init__(self, sigma_u: int, sigma_y: int, tau_u: int, p_b: int):
        self.sigma_u: int = sigma_u
        self.sigma_y: int = sigma_y
        self.tau_u: int = tau_u
        self.p_b: int = p_b


class Aluminum6061T6(Metal):
    def __init__(self):
        sigma_u = 29.5  # kg/mm^2
        sigma_y = 24.6  # kg/mm^2
        tau_u = 19  # kg/mm^2
        p_b = 62  # kg/mm^2
        super(Aluminum6061T6, self).__init__(sigma_u, sigma_y, tau_u, p_b)


class Aluminum2024T3Sheet(Metal):
    def __init__(self):
        sigma_u = 42  # kg/mm^2
        sigma_y = 27.4  # kg/mm^2
        tau_u = 26.7  # kg/mm^2
        p_b = 78  # kg/mm^2
        super(Aluminum2024T3Sheet, self).__init__(sigma_u, sigma_y, tau_u, p_b)


class Aluminum2024T3Extrusion(Metal):
    def __init__(self):
        sigma_u = 40  # kg/mm^2
        sigma_y = 30  # kg/mm^2
        tau_u = 21  # kg/mm^2
        p_b = 76  # kg/mm^2
        super(Aluminum2024T3Extrusion, self).__init__(sigma_u, sigma_y, tau_u, p_b)


def kuhn_diagonal_factor(tao, tao_cr):
    return math.tanh(0.5 * math.log10(tao / tao_cr))
