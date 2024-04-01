#!/usr/bin/env python3
"""module of a function that takes"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start and end indexes for pagination.

    Parameters:
        page(int): The current page number (1-indexed).
        page_size(int): The number of items per page.

    Returns:
        tuple containing the start index and end index for pagination
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
