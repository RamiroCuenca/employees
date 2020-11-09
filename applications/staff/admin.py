from django.contrib import admin

from .models import Staff, Skills

# Register your models here.
admin.site.register(Skills)

class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'department',
        'avatar',
        # 'skills', Cant add ManyToManyField
    )

    search_fields = ('first_name',) # Determines based on which attribute the records will be sorted

    list_filter = ('job',) # Determines based on which attribute the records will be filtered


admin.site.register(Staff, StaffAdmin)