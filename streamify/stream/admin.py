from django.contrib import admin
from .models import user_profile,movies
# Register your models here.
admin.site.register(user_profile)
admin.site.register(movies)