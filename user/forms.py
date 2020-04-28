from django import forms

from user.models import RegisterModel
from user.models import Post_Complaint
from user.models import Notification
class RegisterForms(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=("name","userid","password","mobilenum","email","gender","profile_pic")

class ComplaintForms(forms.ModelForm):
    class Meta:
        model=Post_Complaint
        fields=("category","title","img","description","location")

class NotificationForms(forms.ModelForm):
    class Meta:
        model=Notification
        fields=("N_title","N_img","N_description")

