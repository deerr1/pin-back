from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from pins.models import Pin

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__+".pin"])
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@INDEX.doc_type
class PinDocument(Document):
    id = fields.IntegerField(attr='id')
    name = fields.TextField(
    )
    description = fields.TextField(
    )
    image = fields.FileField()
    upload_date = fields.DateField()
    user = fields.TextField(
        attr='user_indexing',
    )
    board = fields.TextField(
        attr='board_indexing',
        multi=True
    )
    class Django(object):
        model = Pin