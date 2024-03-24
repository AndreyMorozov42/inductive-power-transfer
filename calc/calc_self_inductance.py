import numpy as np


def self_inductance_turn(r, r_turn):
    # vacuum permeability
    mu0 = 4 * np.pi * 10 ** (-7)
    a = np.log(8 * r / r_turn)
    b = r_turn ** 2 / (8 * r ** 2)
    return mu0 * r * (a - 7 / 4 + b * (a + 1 / 3))


def self_inductance(coil, r_turn, N=60, K=60):
    mu0 = 4 * np.pi * 10 ** (-7)
    l = np.sum(self_inductance_turn(r=coil, r_turn=r_turn))
    d, ro, fi = 0, 0, 0
    n = np.arange(N)
    k = n.reshape((K, 1))
    df1 = 2 * np.pi / N
    df2 = 2 * np.pi / K
    mutual_inductance = 0
    for ri in range(len(coil)):
        for rj in range(len(coil)):
            if ri != rj:
                M = 0

                xk_xn = ro + coil[ri] * np.cos(df2 * k) * np.cos(fi) - coil[rj] * np.cos(df1 * n)
                yk_yn = coil[ri] * np.sin(df2 * k) * np.cos(fi) - coil[rj] * np.sin(df1 * n)
                zk_zn = d + coil[ri] * np.cos(df2 * k) * np.sin(fi)

                r12 = (xk_xn ** 2 + yk_yn ** 2 + zk_zn ** 2) ** 0.5

                M += (np.cos(df2 * k - df1 * n) * df1 * df2) / r12
                M *= mu0 * coil[ri] * coil[rj] / (4 * np.pi)
                mutual_inductance += np.sum(M)
    l += mutual_inductance
    return l




