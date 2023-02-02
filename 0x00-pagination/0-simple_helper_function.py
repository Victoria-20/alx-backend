#!/usr/bin/env python3
""" Helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an
    end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters."""

    if page == 1:
        return (0, page_size)

    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
