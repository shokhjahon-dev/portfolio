from django.contrib import admin
from .models import Education, Experience, Awards

# Register your models here.
admin.site.register([Education, Experience,Awards])