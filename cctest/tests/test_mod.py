import os
import pytest

from ..mod import f

@pytest.fixture
def no_txt_dir(tmp_path):
    with open(tmp_path / 'no.txt', 'x'):
        pass
    return tmp_path
    

def test_f(tmp_path):
    exp = 42
    f(tmp_path)
    with open((tmp_path / 'yes.txt'), 'r') as fhandle:
        obs = int(fhandle.read())
    assert obs == exp


def test_f_with_no(no_txt_dir):
    f(no_txt_dir)
    assert not (no_txt_dir / 'yes.txt').exists()
