from django.contrib import admin
from .models import *

admin.site.register(Board)
admin.site.register(AccessToBoard)
admin.site.register(UserRightBoard)
admin.site.register(PinCategory)
admin.site.register(Pin)
admin.site.register(BoardPin)

