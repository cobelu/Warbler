class Metal:
    def __init__(self, sigma_u, sigma_y, tau_u, p_b):
        self.sigma_u = sigma_u
        self.sigma_y = sigma_y
        self.tau_u = tau_u
        self.p_b = p_b


class Aluminum6061T6(Metal):
    def __init__(self):
        sigma_u = 29.5  # kg/mm^2
        sigma_y = 24.6  # kg/mm^2
        tau_u = 19  # kg/mm^2
        p_b = 62  # kg/mm^2
        super().__init__(sigma_u, sigma_y, tau_u, p_b)
