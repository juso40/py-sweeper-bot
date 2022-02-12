from typing import Dict
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

import cv2
import numpy as np
import PIL.ImageGrab as pig

BoundingRect = Tuple[int, int, int, int]


def get_screen_gray() -> np.ndarray:
    img = np.array(pig.grab())
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img_gray


def get_contours(img: np.ndarray) -> Tuple[np.ndarray, ...]:
    ret, thresh = cv2.threshold(img, 150, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def contours_to_rects(
    contours: Iterable[np.ndarray], n: int
) -> Union[None, List[BoundingRect]]:
    areas: Dict[int, List[float]] = {}
    for c in contours:
        areas.setdefault(cv2.contourArea(c), []).append(c)

    for k, v in areas.items():
        if len(v) == n:
            return [cv2.boundingRect(cnt) for cnt in v]


def get_rect_origin(rects: Iterable[BoundingRect]) -> BoundingRect:
    origin = min(rects, key=lambda rect: rect[0] + rect[1])
    return origin
