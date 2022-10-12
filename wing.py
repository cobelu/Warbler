from dataclasses import dataclass
from basics import Basics
from util import FOS
from fuselage import Fuselage


@dataclass
class Wing:
    area: float  # m^2
    wingspan: float  # m
    wingtip_l: float  # m
    web_t: float  # mm
    cap_t: float  # mm
    cap_h: float  # mm
    cap_w: float  # mm
    doubler_t: float  # mm
    wing_w: int  # kg

    def _l(self, fuselage: Fuselage):
        return (self.wingspan - fuselage.cabin_width) / 2

    def p(self, basics: Basics, fuselage: Fuselage):
        return (1.05 * (basics.w - self.wing_w) * basics.n * FOS) / self._l(fuselage)

    def q(self, basics: Basics, fuselage: Fuselage):
        return self.p(basics, fuselage) * self._l(fuselage)

    def m(self, basics: Basics, fuselage: Fuselage):
        return self.q(basics, fuselage) * self._l(fuselage) / 2

    def area_of_compression(self):
        return self.cap_h * (self.doubler_t + self.web_t + self.cap_t) + self.cap_t * (self.cap_w - self.cap_t)

    def web_shear_stress(self):
        pass

    def k_upright(self):
        pass

    def web_shear_flow(self):
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
