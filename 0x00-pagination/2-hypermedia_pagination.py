#!/usr/bin/env python3
"""2. Hypermedia pagination"""

import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """  method named get_page that takes two integer arguments page """
        self.dataset()
        if len(self.__dataset) == 0:
            return[]
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        ind_debut, index_end = index_range(page, page_size)
        return(self.__dataset[ind_debut: index_end])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function a get_hyper method that takes the same arguments (and
            defaults) as get_page and returns a dicttionary containing the
            following key-value pairs"""

        dict = {}

        dict['page_size'] = page_size
        dict['page'] = page
        dict['data'] = self.get_page(page, page_size)

        _lenset = len(self.__dataset)

        if (page + page_size) < _lenset:
            dict['next_page'] = None
        else:
            dict['next_page'] = page + 1

        if (page - page_size) > 1:
            dict['prev_page'] = page - 1
        else:
            dict['prev_page'] = None

        dict['total_pages'] = math.ceil(_lenset / page_size)

        return dict
