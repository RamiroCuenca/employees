from django.contrib import admin

from .models import Staff, Skills

# Register your models here.
admin.site.register(Skills)

class StaffAdmin(admin.ModelAdmin):
    # List_Display determines wich fields will be shown at the screen
    list_display = (
        'first_name',
        'last_name',
        'job',
        'description',
        'department_tag',
        'avatar',
        'full_name', # It does not exist, we may create it with a funcion
        'id',
        # 'skills', Cant add ManyToManyField
    )

    def department_tag(self, obj):
        ''' Creates the name of the department '''
        #print(obj.department)
        return obj.department.name + ' - ' + obj.department.tag
    #
    def full_name(self, obj):
        ''' Creates full name attribute '''
        # obj return the first_name, the last_name and the id of the employee
        full_name = obj.first_name + ' ' + obj.last_name
        return full_name
    #
    search_fields = ('first_name',) # Determines based on which attribute the records will be sorted
    list_filter = ('job', 'skills',) # Determines based on which attribute the records will be filtered
    #
    filter_horizontal = ('skills',)

admin.site.register(Staff, StaffAdmin)