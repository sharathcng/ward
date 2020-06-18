from django import forms

from user.models import RegisterModel
from user.models import Post_Complaint
from user.models import Notification

class RegisterForms(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=("name","userid","password","mobilenum","email","gender","profile_pic")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if (name == ""):
            raise forms.ValidationError('This field cannot be blank')
        return name
    
    def clean_userid(self):
        userid = self.cleaned_data.get('userid')
        if (userid == ""):
            raise forms.ValidationError('This field cannot be blank')

        for instance in RegisterModel.objects.all():
            if instance.userid == userid:
                raise forms.ValidationError('The id ' + userid +' already exists')
        return userid
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if (password == ""):
            raise forms.ValidationError('This field cannot be blank')
    
        for instance in RegisterModel.objects.all():
            if instance.password == password:
                raise forms.ValidationError('Password already exists! Plz use unique pass****')
        return password
    
    def clean_mobilenum(self):
        mobilenum = self.cleaned_data.get('mobilenum')
        if (mobilenum == ""):
            raise forms.ValidationError('This field cannot be blank')
    
        for instance in RegisterModel.objects.all():
            if instance.mobilenum == mobilenum:
                raise forms.ValidationError('{} already exists!'.format(mobilenum))
        return mobilenum
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (email == ""):
            raise forms.ValidationError('This field cannot be blank')
    
        for instance in RegisterModel.objects.all():
            if instance.email == email:
                raise forms.ValidationError('{}, this email already exists. Plz enter a valid email'.format(email))
        return email
    




class ComplaintForms(forms.ModelForm):
    class Meta:
        model=Post_Complaint
        fields=("category","title","img","description","location")

class NotificationForms(forms.ModelForm):
    class Meta:
        model=Notification
        fields=("N_title","N_img","N_description")

    