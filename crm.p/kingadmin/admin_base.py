import json
from django.shortcuts import render


class BaseKingAdmin(object):

    def __init__(self):
        if 'delete_selected_objs' not in self.actions:  #会出现多个删除，就需要进行有的判断
            self.actions.extend(self.default_actions)

    list_display = []
    list_filter = []
    search_fields = []

    readonly_fields = []
    filter_horizontal = []
    list_per_page = 5  # 修改分页（设置默认显示多少条数据）
    default_actions = ['delete_selected_objs']
    actions = []

    def delete_selected_objs(self, request, querysets):
        querysets_ids = json.dumps([i.id for i in querysets])

        return render(request, 'kingadmin/table_obj_delete.html', {'admin_class': self,  # self就是admin_class
                                                                   'objs': querysets,
                                                                   'querysets_ids': querysets_ids
                                                                   })
