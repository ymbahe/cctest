import pytest
import numpy as np


@pytest.fixture
def peak():
    """Construct a 1D Gaussian peak."""
    x = np.linspace(-10, 10, num=21)
    sigma = 3.0
    peak = np.exp(-(x / sigma)**2 / 2) / (sigma * np.sqrt(2 * np.pi))
    return peak
