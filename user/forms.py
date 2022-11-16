from django.forms import ModelForm
from .models import*
from django.contrib.auth.forms import UserChangeForm
class ProfilForm(ModelForm):
    class Meta:
        model =Profil
        fields=["isim","resim"]
    def __init__(self, *args , **kwargs):
        super(ProfilForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})

class UserForm(ModelForm):
    class Meta:
        model = User
        fields=['username','email']
    def __init__(self, *args , **kwargs):
        super(UserForm , self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})    