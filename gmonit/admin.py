from django.contrib import admin
from .models import Report, Worker, Mine, Camera



# Register your models here.
admin.site.register(Report)
admin.site.register(Worker)
admin.site.register(Mine)
admin.site.register(Camera)