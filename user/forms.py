from django import forms

from user.models import RegisterModel
from user.models import Post_Complaint

class RegisterForms(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=("name","userid","password","mobilenum","email","gender","profile_pic")

class ComplaintForms(forms.ModelForm):
    class Meta:
        model=Post_Complaint
        fields=("category","title","img","description","location")