import re

def is_valid_project_name(name):
    if not isinstance(name, str) or not name:
        return False

    return bool(re.fullmatch(r"[A-Za-z0-9_-]+", name))
