from . import models
from kingadmin.sites import site


print('student kingadmin ....')


class TestAdmin(object):
    list_display = ['name']


site.register(models.Test, TestAdmin)