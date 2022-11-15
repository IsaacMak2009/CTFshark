from typing import Any
from . import Text, Img

class Binary:
    '''
    ctfshark.util.Binary
    '''
    def __init__(self, path_or_data: Any):
        if not isinstance(path_or_data, (Binary, str)): 
            raise TypeError(
                f"type of 'path_or_data' must be ctfshark.util.Binary or 'str'(path)"
                f"not '{type(path_or_data).__name__}'"
            )

        if isinstance(path_or_data, str):
            self._data = path_or_data._data
        else:
            self._data = None
            with open(path_or_data, 'rb') as f:
                self._data = f.read()

    def getData(self):
        return self._data

    def __repr__(self):
        return f"Binary(...)"