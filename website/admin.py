from django.contrib import admin
from .models import Experience
from .models import Awards
from .models import Leadership

# Register your models here.
admin.site.register(Experience)
admin.site.register(Awards)
admin.site.register(Leadership)