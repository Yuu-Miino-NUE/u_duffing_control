import numpy as np
from scipy.integrate import solve_ivp


def duffing_ode(t, vect, params):
    x, y = vect
    k, B0, B = (params[k] for k in ("k", "B0", "B"))
    return np.array([y, -k * y - x**3 + B0 + B * np.cos(t)])


def solve_duffing_ivp(vect, params, nmap=1, method="DOP853", rtol=1e-8, **kwargs):
    func = lambda t, y: duffing_ode(t, y, params)
    sol = solve_ivp(
        func, (0, 2 * np.pi * nmap), vect, method=method, rtol=rtol, **kwargs
    )
    return sol
