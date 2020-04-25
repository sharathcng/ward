from django.shortcuts import render,redirect,get_object_or_404
import smtplib
from django.db import IntegrityError
from user.forms import RegisterForms
from user.forms import ComplaintForms
from user.forms import NotificationForms
from user.models import RegisterModel
from user.models import Post_Complaint
from user.models import Notification
from user.models import ForwardedModel
from django.core.mail import send_mail
from math import ceil


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
            n = len(complaints)
            nSlides = n//4 + ceil((n/4)-(n//4))
            context = {'no_of_slides':nSlides, 'range': range(1,nSlides),"complaints":complaints,"obje":us_id}
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
    n = len(complaints)
    nSlides = n//4 + ceil((n/4)-(n//4))
    context = {'no_of_slides':nSlides, 'range': range(1,nSlides),"complaints":complaints}
    return render(request, 'index.html',context)



def user_page(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    return render(request, 'login.html', {'obje': us_id})

def comp(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)

    allProds = []
    catprods = Post_Complaint.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Post_Complaint.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds,"obje":us_id}
    return render(request, 'comp.html', params)



    # complaints = Post_Complaint.objects.all()
    # n = len(complaints)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # context = {'no_of_slides':nSlides, 'range': range(1,nSlides),"complaints":complaints,"obje":us_id}
    # return render(request, 'comp.html', context)


# def comp(request):
#     products = Product.objects.all()
#     print(products)
#     n = len(products)
#     nSlides = n//4 + ceil((n/4)-(n//4))
#     params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
#     return render(request, 'shop/index.html', params)



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
    allProds = []
    catprods = ForwardedModel.objects.values('category2', 'id')
    cats = {item['category2'] for item in catprods}
    for cat in cats:
        prod = ForwardedModel.objects.filter(category2=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds,"obje":us_id}
    return render(request, 'forComplaints.html', params)
    



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


def send_email(request,pk):
    pr = Post_Complaint.objects.get(id=pk)
    cid = pr.id
    c = pr.category
    t = pr.title
    d = pr.description
    l = pr.location
    i = pr.img  
    content = c+"\n"+t+"\n"+d+"\n"+l
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('cngsharath@gmail.com', '9480473080')
    if c == "Garbage" :
        mail.sendmail( 'cngsharath@gmail.com', 'sachin.s.kabadi10@gmail.com',content)
    elif c == "Sanitory":
        mail.sendmail( 'cngsharath@gmail.com','sknamrathagowda@gmail.com', content)
    elif c == "Electricity":
        mail.sendmail( 'cngsharath@gmail.com','www.namrathaskgowda@gmail.com', content)
    else:
        mail.sendmail('cngsharath@gmail.com', 'cngsharath@gmail.com', content)
    mail.close()
    ForwardedModel.objects.create(userd=cid,category2=c,title2=t,img2=i,description2=d,location2=l)
    return redirect('admin')