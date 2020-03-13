import xadmin
from xadmin import views


from .models import EmailVerifyRecord,Banner

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']

    search_fields = ['code', 'email', 'send_type']

    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)



class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)


class BaseSetting(object):

    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)



class GlobalSettings(object):

    site_title = 'Xspace载人航天管理平台'

    site_footer= 'XSPACE.'

    menu_style = 'accordion'   # 收起菜单

xadmin.site.register(views.CommAdminView, GlobalSettings)








