#!/usr/bin/env python3
""" The function simplify Pagination
"""


def index_range(page, page_size):
    """Returns the index range for the page"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
