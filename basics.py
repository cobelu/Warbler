import math


class Basics:
    def __init__(self, n_1, bhp, s, w):
        self.n_1 = n_1
        self.w = w
        self.s = s
        self.bhp = bhp
        self.wing_loading = self.w / self.s

    def n_2(self):
        return - (1 / 2) * self.n_1

    def n_3(self):
        # See ASTM
        limit = 108  # kg/m^2
        if self.n_1 * self.wing_loading > limit:
            return self.n_1

    def n_4(self):
        n_3 = self.n_3()
        return n_3 / 2

    def n_f(self):
        return self.n_1 / 2

    def _v_multiplier(self):
        return math.sqrt(self.n_1 * self.wing_loading)

    def v_f_mini(self):
        return 11 * self._v_multiplier()

    def v_a_mini(self):
        return 15 * self._v_multiplier()

    def v_c_mini(self):
        return max(15 * self._v_multiplier(), 0.9 * self.v_h())

    def v_d_mini(self):
        return max(24 * self._v_multiplier(), 1.3 * self.v_c_mini())

    # -------------------------
    # Limit Loads
    # -------------------------

    def w_vt(self):
        # TODO: Fix units
        limit = self.n_1 * self.wing_loading  # psf -> kg/m^2:
        if limit < 47:
            return 3.66 * self._v_multiplier()
        else:
            return 0.534 * limit  # TODO: Convert PSF -> kg/m^2

    def w_ht(self):
        return 4.8 + 0.534 * self.n_1 * self.wing_loading

    def w_tab(self):
        # TODO: Implement this
        pass

    def w_f(self):
        # TODO: Implement this
        pass

    def w_a(self):
        # TODO: Implement this
        limit = self.n_1 * self.wing_loading
        return 0.466 * limit


def v_h(self):
    return 150 * math.pow(self.bhp / (self.s + 8), 1 / 3)


def v_z(self):
    return 26 * self.bhp / self.w


def z_max(self):
    return 950 * self.v_z()
