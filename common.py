import sys


def get_resource_path(path: str | None) -> str:
    try:
        return sys._MEIPASS + '/' if path is None else sys._MEIPASS + f'/{path}'
    except AttributeError:
        pass
    return path

