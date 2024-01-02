#!/usr/bin/env python3
"""
0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    function that returns a tuple containing a start index and end index
    corresponding to the range of indexes to return in a list
    Args:
        page - int, page number
        page_size - int, page size
    Returns:
        Tuple
    """
    if page <= 0 or page_size <= 0:
        return None
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
