from checker import is_valid_project_name

def test_valid_project_name():
    assert is_valid_project_name("my-project") == True
