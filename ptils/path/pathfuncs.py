""" Path Utility functions """

import os
from collections.abc import Generator


def list_with_path(path: str) -> Generator[str, None, None]:
    return (os.path.join(path, list_item) for list_item in os.listdir(path))
