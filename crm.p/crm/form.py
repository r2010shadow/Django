from django.forms import ModelForm
from crm import models


#静态ModelForm增加自定样式的写法


class CustomerForm(ModelForm):
    class Meta:
        model = models.CustomerInfo
        fields = "__all__"

    def __new__(cls, *args, **kwargs):
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]
            field_obj.widget.attrs.update({'class':'form-control'})


        return ModelForm.__new__(cls)

