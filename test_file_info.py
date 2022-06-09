import pytest
import get_file_info

@pytest.mark.parametrize('root_dir, filename', [('D:\\SIM\\Projetos\\FG_Telem', None)])
def test_file(root_dir, count):
  assert get_file_info.request(root_dir) == filename
