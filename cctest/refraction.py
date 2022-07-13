# cctest/refraction.py

import numpy as np


def snell(theta_inc, n1, n2):
    """
    Compute the refraction angle using Snell's Law.

    See https://en.wikipedia.org/wiki/Snell%27s_law

    Parameters
    ----------
    theta_inc : float
        Incident angle in radians.
    n1, n2 : float
        The refractive indices of medium or origin and destination.

    Returns
    -------
    theta : float
        Refraction angle

    Examples
    --------
    A ray enters an air-water boundary at pi/4 radians (i.e. 45 degrees).
    Compute the exit angle.

    >>> snell(np.pi / 4, 1.0, 1.33)
    0.560558
    """
    return np.arcsin(n1 / n2 * np.sin(theta_inc))
