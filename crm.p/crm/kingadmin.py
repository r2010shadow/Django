from kingadmin.sites import site
from crm import models
from kingadmin.admin_base import BaseKingAdmin

print('crm kingadmin ...')


class CustomerAdmin(BaseKingAdmin):
    list_display = ['name', 'source', 'contact_type', 'contact', 'consultant', 'consult_content', 'status', 'date']
    list_filter = ['source', 'consultant', 'status', 'date']
    search_fields = ['contact', 'consultant__name']
    readonly_fields = ['contact', 'status']
    filter_horizontal = ['consult_courses']

    actions = ['change_status',]

    def change_status(self, request, querysets): #querysets是选中的所有对象
        querysets.update(status=1)


site.register(models.CustomerInfo, CustomerAdmin)
site.register(models.Role)
site.register(models.Menus)
site.register(models.UserProfile)
