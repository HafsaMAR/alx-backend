#!/usr/bin/env python3
"""Simple pagination"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Return a tuple containing the start and end indexes for pagination.

        Parameters:
            page(int): The current page number (1-indexed).
            page_size(int): The number of items per page.

        Returns:
            tuple containing the start index and end index for pagination
        """
        total_items = len(self.dataset())
        start_index = (page - 1) * page_size
        if start_index >= total_items:
            return (0, 0)  # Return an empty tuple it out of ranfe
        end_index = min(start_index + page_size, total_items)
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data of the dataset

        Parameters:
            page(int): The current page number (1-indexed).
            page_size(int): The number of items per page.

        Returns:
            List[list] : A list containing the data for specified page."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = self.index_range(page, page_size)
        # if start == (0, 0):
        #     return []
        return self.dataset()[start:end]
