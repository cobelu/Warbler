from structure import Metal


def ult_margin_of_safety(sigma, metal: Metal):
    return (metal.sigma_u / sigma) - 1


def yield_margin_of_safety(sigma, metal: Metal):
    return (metal.sigma_y / sigma) - 1


def does_fail(sigma, metal: Metal):
    return ult_margin_of_safety(sigma, metal) > 1


def does_yield(sigma, metal: Metal):
    return ult_margin_of_safety(sigma, metal) > 1


FOS = 1.5
