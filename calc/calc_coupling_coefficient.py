import numpy as np

from calc.calc_mutual_inductance import mutual_inductance
from calc.calc_self_inductance import self_inductance


def coupling_coefficient(coil_1, r1_turn, coil_2, r2_turn, d, po, fi):
    l_1 = self_inductance(coil_1, r1_turn)
    l_2 = self_inductance(coil_2, r2_turn)
    m = mutual_inductance(coil_1, coil_2, d, po, fi)
    return m / np.sqrt(l_1 * l_2)