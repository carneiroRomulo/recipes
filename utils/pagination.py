import math


def make_pagination_range(page_range, page_quantity, page_current):
    middle_range = math.ceil(page_quantity / 2)
    start_range = 0
    stop_range = page_quantity

    if page_current > middle_range:
        start_range = page_current - middle_range
        stop_range = page_current + middle_range

    return page_range[start_range: stop_range]
