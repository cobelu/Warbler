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

    def b(self, fuselage: Fuselage):
        return (self.wingspan - fuselage.cabin_width) / 2

    def q(self, basics: Basics, fuselage: Fuselage, eta: float):
        return (1.05 * (basics.w - self.wing_w) * eta * FOS) / self.b(fuselage)

    def area_of_compression(self):
        return self.cap_h * (self.doubler_t + self.web_t + self.cap_t) + self.cap_t * (self.cap_w - self.cap_t)
