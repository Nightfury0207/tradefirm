from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Order_Parent)
admin.site.register(Order_Child)
admin.site.register(Dispatch_Parent)
admin.site.register(Dispatch_Child)
admin.site.register(Inward_Parent)
admin.site.register(Inward_Child)