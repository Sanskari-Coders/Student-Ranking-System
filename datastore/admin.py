from django.contrib import admin
from datastore.models import Student
from datastore.models import data_store
# Register your models here.
admin.site.register(Student)
admin.site.register(data_store)