import pytest
import routines

@pytest.mark.parametrize('seq, count', [([0,0,1,1], 1), ([0,1,0], 0), ([0,1], 0), ([0,0,0,1,1], 2)])
def test_count_coin(seq, count):
  assert routines.count_coin_flips(seq) == count
