from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    CompoundSearchFilterBackend,
    SearchFilterBackend,
    MultiMatchSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents import PinDocument
from .serializers import PinDocumentSerializer

class PinDocumentView(BaseDocumentViewSet):
    document = PinDocument
    serializer_class = PinDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        MultiMatchSearchFilterBackend
    ]

    multi_match_search_fields = {
        'user': {'boost': 4},
        'name': {'boost': 4},
        'description': {'boost': 4},
    }
    # search_fields = {
    #     'user',
    #     'name',
    #     'description',
    # }
    multi_match_options = {
        'type': 'phrase_prefix'
    }
    filter_fields = {
        'id': 'id',
        'name': 'name',
        'user': 'user',
        'upload_date': 'upload_date',
    }
    ordering_fields = {
        'id': 'id',
        'name': 'name',
        'upload_date': 'upload_date',
    }