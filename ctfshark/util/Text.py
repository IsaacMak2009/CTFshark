from typing import Any
from . import Binary, Img

class Text:
    '''
    ctfshark.util.Text
    '''
    def __init__(self, text: Any):
        if not isinstance(text, (str, Text)): 
            raise TypeError(
                f"type of 'text' must be 'ctfshark.util.Text' or 'str'"
                f"not '{type(text).__name__}'"
            )

        if isinstance(text, str):
            self._text = text
        else:
            self._text = text._text

    def getText(self):
        return self._text

    def __len__(self):
        return len(self._text)

    def __repr__(self):
        return f"Text(\"{self._text}\")"