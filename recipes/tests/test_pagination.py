from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination)
