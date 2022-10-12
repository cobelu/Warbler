class Hardware:
    def __init__(self, diameter: float, ult_shear: int, ult_tension: int):
        self.diameter: float = diameter
        self.ult_shear: int = ult_shear
        self.ult_tension: int = ult_tension


class Bolt(Hardware):
    def __init__(self, diameter: float, ult_shear: int, ult_tension: int):
        super(Bolt, self).__init__(diameter, ult_shear, ult_tension)


class AN3(Bolt):
    def __init__(self):
        diameter = 4.8  # mm
        ult_shear = 940  # kg
        ult_tension = 1000  # kg
        super(AN3, self).__init__(diameter, ult_shear, ult_tension)


class AN4(Bolt):
    def __init__(self):
        diameter = 6.3  # mm
        ult_shear = 1670  # kg
        ult_tension = 1850  # kg
        super(AN4, self).__init__(diameter, ult_shear, ult_tension)


class AN5(Bolt):
    def __init__(self):
        diameter = 8  # mm
        ult_shear = 2600  # kg
        ult_tension = 2900  # kg
        super(AN5, self).__init__(diameter, ult_shear, ult_tension)


class AN6(Bolt):
    def __init__(self):
        diameter = 9.5  # mm
        ult_shear = 3700  # kg
        ult_tension = 4500  # kg
        super(AN6, self).__init__(diameter, ult_shear, ult_tension)


class AN7(Bolt):
    def __init__(self):
        diameter = 11.1  # mm
        ult_shear = 5100  # kg
        ult_tension = 6100  # kg
        super(AN7, self).__init__(diameter, ult_shear, ult_tension)


class AN8(Bolt):
    def __init__(self):
        diameter = 12.7  # mm
        ult_shear = 6600  # kg
        ult_tension = 8400  # kg
        super(AN8, self).__init__(diameter, ult_shear, ult_tension)


class Rivet(Hardware):
    def __init__(self, diameter: float, ult_shear: int):
        super(Rivet, self).__init__(diameter, ult_shear, 0)


class PulledRivet(Hardware):
    def __init__(self, diameter: float, ult_shear: int):
        super(PulledRivet, self).__init__(diameter, ult_shear, 0)


class DrivenRivet(Hardware):
    def __init__(self, diameter: float, ult_shear: int):
        super(DrivenRivet, self).__init__(diameter, ult_shear, 0)


class A4(PulledRivet):
    def __init__(self):
        diameter = 3.2  # mm
        ult_shear = 50  # kg
        super(A4, self).__init__(diameter, ult_shear)


class A5(PulledRivet):
    def __init__(self):
        diameter = 4  # mm
        ult_shear = 80  # kg
        super(A5, self).__init__(diameter, ult_shear)


class AN470AD3(DrivenRivet):
    def __init__(self):
        diameter = 2.4  # mm
        ult_shear = 95  # kg
        super(AN470AD3, self).__init__(diameter, ult_shear)


class AN470AD4(DrivenRivet):
    def __init__(self):
        diameter = 3.1  # mm
        ult_shear = 150  # kg
        super(AN470AD4, self).__init__(diameter, ult_shear)


class AN470AD5(DrivenRivet):
    def __init__(self):
        diameter = 4  # mm
        ult_shear = 250  # kg
        super(AN470AD5, self).__init__(diameter, ult_shear)


class AN470AD6(DrivenRivet):
    def __init__(self):
        diameter = 4.8  # mm
        ult_shear = 360  # kg
        super(AN470AD6, self).__init__(diameter, ult_shear)
