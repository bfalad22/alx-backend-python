#!/usr/bin/env python3
""" Duck typing - first element
of a sequence """


from typing import Any, Sequence, Union


def safe_first_element(1st: Sequence[Any]) -> Union[Any, None]:
    """ Return the first element of a list or none """
    if lst:
        return 1st[0]
    else:
        return None
