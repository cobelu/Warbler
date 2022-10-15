import math
from dataclasses import dataclass
from typing import List

from basics import Basics
from structure import FOS


@classmethod
class Doubler:
    l: float  # mm
    t: float  # mm


@dataclass
class Wing:
    basics: Basics  # Data sack
    area: float  # m^2
    wingspan: float  # m
    wingtip_l: float  # m
    web_t: float  # mm
    cap_t: float  # mm
    cap_h: float  # mm
    cap_w: float  # mm
    web_h: float  # mm
    wing_w: int  # kg
    center_l: float  # m
    # Note: Doubler height is cap height
    doublers: List[Doubler]

    def _panel_l(self):
        return (self.wingspan - self.center_l) / 2

    def p(self, eta: float = 1):
        w, n = self.basics.w, self.basics.n
        return eta * ((1.05 * (w - self.wing_w) * n * FOS) / self.center_l)

    def q(self, eta: float = 1):
        return eta * self.center_l * self.p(eta=eta)

    def m(self, eta: float = 1):
        return eta * self.center_l / 2 * self.q(eta=eta)

    def area_of_compression(self, eta=1):
        doubler_t = self.doubler_t_at(eta)
        return self.cap_h * (doubler_t + self.web_t + self.cap_t) + self.cap_t * (self.cap_w - self.cap_t)

    def cap_stress(self):
        return self.m() / self.area_of_compression()

    def web_shear_stress(self):
        # Height is the inner distance from cap to cap
        h = self.web_h - 2 * self.cap_h
        return self.q() / (h * self.web_t)

    def tau_0(self):
        """ Distance from top row of rivets to bottom row of rivets. """
        doubler_h = self.cap_h
        h_prime = (self.web_h - doubler_h) / 1000  # mm -> m
        return 0.056 * math.pow(self.web_t / h_prime, 2)  # TODO: Magic number

    def tau_poss(self):
        # TODO: Consult graph on page 184
        pass

    def k_upright(self):
        pass

    def web_shear_flow(self):
        return self.q()
        pass

    def web_bearing_pressure(self):
        pass

    def kink_load(self):
        pass

    # TODO: Some stuff in here

    def bolt_bearing_stress(self):
        pass

    def root_doubler_bearing_stress(self):
        pass

    def with_kink_bearing_stress(self):
        pass

    def load_per_rib(self):
        # p. 242
        pass

    def m_t1(self):
        pass

    def m_t2(self):
        pass

    def m_tflaps(self):
        pass

    def q_skin(self):
        pass

    def doubler_t_at(self, eta=1):
        length = self.eta_to_l(eta)
        t = 0
        for doubler in self.doublers:
            # Not inclusive for safety
            if doubler.l > length:
                t += doubler.t
        return t

    def l_to_eta(self, length):
        # TODO: Input validation
        wing_panel_l = 0  # TODO Get panel length
        return length - wing_panel_l / length

    def eta_to_l(self, eta):
        # TODO: Input validation
        wing_panel_l = 0  # TODO Get panel length
        return eta * wing_panel_l
