from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_correct_pagination_range(self):
        """When current page is bigger than (page_quantity / 2)
        pagination range should change"""

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=2,
        )
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=3,
        )
        self.assertEqual([2, 3, 4, 5], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=4,
        )
        self.assertEqual([3, 4, 5, 6], pagination)
