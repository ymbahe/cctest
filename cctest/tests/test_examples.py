import numpy as np
import pytest
from ..refraction import snell


def test_one_plus_one_is_two():
    "Check that one and one are indeed two."
    assert 1 + 1 == 2


@pytest.mark.parametrize(
    'n1, n2',
    [(2.0, 3.0), (3.0, 2.0)]
)
def test_perpendicular(n1, n2):
    """Test that a perpendicular ray is not bent."""

    actual = snell(0, n1, n2)
    expected = 0
    assert actual == expected


def test_air_water():
    """Test the expected refraction angle for one particular situation."""

    n_air, n_water = 1.0, 1.33
    actual = snell(np.pi / 4, n_air, n_water)
    expected = 0.560558
    assert np.allclose(actual, expected)
