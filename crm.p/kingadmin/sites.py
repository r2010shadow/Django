
from kingadmin.admin_base import BaseKingAdmin

class AdminSite(object):
    def __init__(self):
        self.enable_admins = {}

    def register(self, model_class, admin_class=None):
        app_name = model_class._meta.app_label
        model_name = model_class._meta.model_name

        if not admin_class:
            admin_class = BaseKingAdmin()
        else:
            admin_class = admin_class()
        admin_class.model = model_class

        if app_name not in self.enable_admins:
            self.enable_admins[app_name] = {}
        self.enable_admins[app_name][model_name] = admin_class


site = AdminSite()

