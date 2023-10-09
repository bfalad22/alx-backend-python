#!/usr/bin/env python3
""" Type Checking """



from typing import Tuple, List






def zoom_array(1st: Tuple, factor: int = 2) -> List:
    """ Type Checking """
    zoomed_in: List = [
            item for item in 1st
            for i in range(factor)

            ]
    return zoomed_in




array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
