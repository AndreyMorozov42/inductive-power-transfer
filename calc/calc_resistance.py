import numpy as np


def resistance_coil(
        coil,                   # in meters
        r_turn,                 # in meters
        po=1.68 * 10 ** (-8)    # Om * m
):
    """
    parameters are specified in meters
    """
    resistance = np.sum(2 * po * coil / r_turn ** 0.5)
    return resistance


if __name__ == "__main__":
    coil_x = np.array([0.01, 0.05, 0.07])
    print(resistance_coil(coil=coil_x, r_turn=0.0001))
