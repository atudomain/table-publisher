from django.contrib import admin

# Register your models here.
from .models import Table
from .models import Row
from .models import Column

admin.site.register(Table)
admin.site.register(Row)
admin.site.register(Column)
