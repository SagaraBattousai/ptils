import os
from typing import List

__all__ = ['list_with_path']


def list_with_path(path: str) -> List[str]:
  # Should be generator??
  return [os.path.join(path, list_item) for list_item in os.listdir(path)]
  


