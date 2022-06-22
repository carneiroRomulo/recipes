import math

from django.core.paginator import Paginator


def make_pagination_range(page_range, page_quantity, page_current):
    middle_range = math.ceil(page_quantity / 2)
    # Static page range near the first pages
    start_range = 0
    stop_range = page_quantity

    if page_current > middle_range:
        if page_current < len(page_range) - middle_range:
            # Dynamic page range
            start_range = page_current - middle_range
            stop_range = page_current + middle_range
        else:
            # Static page range near the last pages
            start_range = len(page_range) - page_quantity
            stop_range = len(page_range)

    pagination = page_range[start_range: stop_range]
    return {
        "pagination": pagination,
        "page_current": page_current,
        "page_range": page_range,
        "total_pages": len(page_range),
        "first_page_out_of_range": page_current > middle_range,
        "last_page_out_of_range":
            page_current < len(page_range) - middle_range,
    }


def pagination(request, queryset, per_page, page_quantity=4):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(queryset, per_page)
    page_object = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        page_quantity=page_quantity,
        page_current=current_page
    )

    return page_object, pagination_range
