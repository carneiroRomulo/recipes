from unittest import TestCase

from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_is_static_near_the_start(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_make_pagination_range_is_static_near_the_end(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

    def test_make_pagination_range_returns_correct_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=13,
        )['pagination']
        self.assertEqual([12, 13, 14, 15], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            page_quantity=4,
            page_current=17,
        )['pagination']
        self.assertEqual([16, 17, 18, 19], pagination)
