import pytest
import routines

@pytest.mark.parametrize('list1, list2, res', [([1], [2], None), ([2], [2], 2), ([3], [2,3], 3), ([], [], None)])
def test_repeated(list1, list2) == res
