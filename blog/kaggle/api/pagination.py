from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
)

class KaggleLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 50
	max_limit = 1000


class KagglePageNumberPagination(PageNumberPagination):
	page_size = 5
