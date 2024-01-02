#!/usr/bin/env python3
"""
0. Simple helper function
"""
from typing import Tuple, List
import csv
import math


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve the specified page of data from the dataset
        """
        assert isinstance(page, int) and page > 0, "should be an integer"
        assert isinstance(page_size, int) and page_size > 0, "should be int"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary with the current dataset page and pagination.
        """
        assert isinstance(page, int) and page > 0, "should be an integer"
        assert isinstance(page_size, int) and page_size > 0, "should be int"

        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_dict = {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        return hyper_dict
