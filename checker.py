def is_valid_project_name(name):
    return (
        isinstance(name, str)
        and len(name.strip()) > 0
    )
