from django.shortcuts import render,redirect,get_object_or_404
import smtplib
from django.db import IntegrityError
from user.forms import RegisterForms
from user.forms import ComplaintForms
from user.forms import NotificationForms
from user.models import RegisterModel
from user.models import Post_Complaint
from user.models import Notification


# Create your views here.

def register(request):
    if request.method=="POST":
        forms=RegisterForms(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            complaints = Post_Complaint.objects.all()
            context = {"complaints":complaints,"obje":user}
            return render(request,'login.html',context)
    else:
        forms=RegisterForms()
    return render(request,'index.html',{'form':forms})


def index(request):
    if request.method=="POST":
        usid=request.POST.get('name')
        pswd = request.POST.get('password')
        if usid == 'admin' and pswd == 'admin':
            check = RegisterModel.objects.get(userid=usid, password=pswd)
            request.session['userid'] = check.id
            us_id = RegisterModel.objects.get(id=check.id)
            complaints = Post_Complaint.objects.all()
            context = {"complaints":complaints,"obje":us_id}
            return render(request,'admin.html',context)
        try:
            check = RegisterModel.objects.get(userid=usid, password=pswd)
            request.session['userid'] = check.id
            us_id = RegisterModel.objects.get(id=check.id)
            complaints = Post_Complaint.objects.all()
            context = {"complaints":complaints,"obje":us_id}
            return render(request,'login.html',context)
        except:
            pass
    complaints = Post_Complaint.objects.all()
    context = {"complaints":complaints}
    return render(request, 'index.html',context)



def user_page(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    return render(request, 'login.html', {'obje': us_id})

def comp(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    complaints = Post_Complaint.objects.all()
    context = {"complaints":complaints,"obje":us_id}
    return render(request, 'comp.html', context)

def admin(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    complaints = Post_Complaint.objects.all()
    context = {"complaints":complaints,"obje":us_id}
    return render(request, 'admin.html', context)

def notification(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    complaints = Post_Complaint.objects.all()
    context = {"complaints":complaints,"obje":us_id}
    return render(request, 'notification.html', context)

def forComp(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    complaints = Post_Complaint.objects.all()
    context = {"complaints":complaints,"obje":us_id}
    return render(request, 'forComplaints.html', context)



def post_comp(request):
    if request.method == "POST":
        forms = ComplaintForms(request.POST, request.FILES)
        if forms.is_valid():
            userid = request.session['userid']
            current_user = RegisterModel.objects.get(id=userid)
            instance = forms.save(commit=False)
            instance.user_id = current_user
            use=instance.save()
            complaints = Post_Complaint.objects.all()
            context = {"complaints":complaints,"obje":use}
            return render(request,'login.html',context)
    else:
        forms = ComplaintForms()
        comp = Post_Complaint.objects.all()
    return render(request, 'login.html', {'obje': forms},{'ob':comp})




def notify(request):
    if request.method == "POST":
        forms = NotificationForms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('admin')
    else:
        forms = ComplaintForms()
    return render(request, 'notification.html', {'form': forms})