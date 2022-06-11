import pytest
import get_file_info


# -----> CHANGE directory name to test <---------
@pytest.mark.parametrize('root_dir, filename', [('C:\\Users\\Windows 10\\Downloads', None)])
def test_file(root_dir, filename):
    assert get_file_info.request(root_dir) == filename
