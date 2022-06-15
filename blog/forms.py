from django.forms import ModelForm
from blog.models import Create


class UserForms(ModelForm):
    class Meta:
        model = Create
        fields = '__all__'
        widgets = {

        }
