from django.shortcuts import render,redirect,get_object_or_404
import smtplib
from django.db import IntegrityError
from user.forms import RegisterForms
from user.forms import ComplaintForms
from user.models import RegisterModel
from user.models import Post_Complaint


# Create your views here.

def register(request):
    if request.method=="POST":
        forms=RegisterForms(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            return render(request,'login.html',{'obje':user})
    else:
        forms=RegisterForms()
    return render(request,'index.html',{'form':forms})


def index(request):
    if request.method=="POST":
        usid=request.POST.get('name')
        pswd = request.POST.get('password')
        try:
            check = RegisterModel.objects.get(userid=usid, password=pswd)
            request.session['userid'] = check.id
            us_id = RegisterModel.objects.get(id=check.id)
            return render(request,'login.html',{'obje':us_id})
        except:
            pass
    return render(request, 'index.html')



def user_page(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    return render(request, 'login.html', {'obje': us_id})


def post_comp(request):
    if request.method == "POST":
        forms = ComplaintForms(request.POST, request.FILES)
        if forms.is_valid():
            userid = request.session['userid']
            current_user = RegisterModel.objects.get(id=userid)
            instance = forms.save(commit=False)
            instance.user_id = current_user
            use=instance.save()
            return render(request, 'login.html', {'obje': use})
    else:
        forms = ComplaintForms()
    return render(request, 'login.html', {'obje': forms})