from typing import Any
from . import Text, Binary
from cv2 import imread
import numpy as np

class Img:
    '''
    ctfshark.util.Img
    '''
    def __init__(self, path_or_img: Any):
        if not isinstance(path_or_img, (Img, str)): 
            raise TypeError(
                f"type of 'path_or_img' must be ctfshark.util.Img, or 'str'(path)"
                f"not '{type(path_or_img).__name__}'"
            )

        if isinstance(path_or_img, str):
            self._img = imread(path_or_img)
        else:
            self._img = path_or_img._img
    
    def getImg(copy=True):
        if copy:
            return self._img.copy()
        return self._img

    def __repr__(self):
        return f"Img(...), shape: {self._img.shape}"