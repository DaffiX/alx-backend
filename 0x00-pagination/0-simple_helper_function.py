#!/usr/bin/env python3
""" The function simplify the process of determine ragne of index
"""
def index_range(page, page_size):
    start = (page - 1) * page_size
    end = page * page_size
    return start, end 