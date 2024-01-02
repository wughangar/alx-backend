#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with current dataset page based on an index.
        """
        assert index is None or (isinstance(index, int)
                                 and index >= 0), "Index should be int"
        assert isinstance(page_size, int) and page_size > 0, "should be an int"

        dataset = self.dataset()
        total_items = len(dataset)
        if index is None:
            index = 0
        else:
            assert index <= total_items, "Index out of range"

        next_index = min(index + page_size, total_items)
        page_data = dataset[index:next_index]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": page_data
        }
