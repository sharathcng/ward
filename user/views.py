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
from user.models import CompletedModel
from math import ceil
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


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
            pending = Post_Complaint.objects.count()
            forwarded = ForwardedModel.objects.count()
            rejected = CompletedModel.objects.filter( status='Rejected' ).count()
            resolved = CompletedModel.objects.filter( status='Resolved' ).count()
            n = len(complaints)
            nSlides = n//4 + ceil((n/4)-(n//4))
            context = {'no_of_slides':nSlides, 'range': range(1,nSlides),"complaints":complaints,"obje":us_id,'pending':pending,'forwarded':forwarded,'rejected':rejected,'resolved':resolved}
            return render(request,'admin.html',context)
        try:
            check = RegisterModel.objects.get(userid=usid, password=pswd)
            request.session['userid'] = check.id
            us_id = RegisterModel.objects.get(id=check.id)
            complaints = Post_Complaint.objects.all()
            notifications = Notification.objects.all()
            pending = Post_Complaint.objects.count()
            forwarded = ForwardedModel.objects.count()
            rejected = CompletedModel.objects.filter( status='Rejected' ).count()
            resolved = CompletedModel.objects.filter( status='Resolved' ).count()
            context = {"complaints":complaints,"obje":us_id,"notifications":notifications,'pending':pending,'forwarded':forwarded,'rejected':rejected,'resolved':resolved}
            return render(request,'login.html',context)
        except:
            pass
    complaints = Post_Complaint.objects.all()
    n = len(complaints)
    nSlides = n//4 + ceil((n/4)-(n//4))
    pending = Post_Complaint.objects.count()
    forwarded = ForwardedModel.objects.count()
    notifications = Notification.objects.all()
    rejected = CompletedModel.objects.filter( status='Rejected' ).count()
    resolved = CompletedModel.objects.filter( status='Resolved' ).count()
    context = {'no_of_slides':nSlides, 'range': range(1,nSlides),"notifications":notifications,"complaints":complaints,'pending':pending,'forwarded':forwarded,'rejected':rejected,'resolved':resolved}
    return render(request, 'index.html',context)

    

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
            complaints = Post_Complaint.objects.all()
            context = {"complaints":complaints,"obje":use}
            return render(request,'login.html',context)
    else:
        forms = ComplaintForms()
        comp = Post_Complaint.objects.all()
    return render(request, 'login.html', {'obje': forms},{'ob':comp})



#Admin section
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

def resolved_complaints(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    allProds = []
    catprods = CompletedModel.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = CompletedModel.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds,"obje":us_id}
    return render(request, 'Resolved_complaints.html', params)



def rejected_complaints(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    allProds = []
    catprods = CompletedModel.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = CompletedModel.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds,"obje":us_id}
    return render(request, 'Rejected_complaints.html', params)


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
    notifications = Notification.objects.all()
    context = {"complaints":complaints,"obje":us_id,"notifications":notifications}
    return render(request, 'notification.html', context)

    


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
    if c == "Garbage":
        mail.sendmail( 'cngsharath@gmail.com', 'sachin.s.kabadi10@gmail.com',content)
    elif c == "Sanitory":
        mail.sendmail( 'cngsharath@gmail.com','sknamrathagowda@gmail.com', content)
    elif c == "Electricity":
        mail.sendmail( 'cngsharath@gmail.com','www.namrathaskgowda@gmail.com', content)
    else:
        mail.sendmail('cngsharath@gmail.com', 'cngsharath@gmail.com', content)
    mail.close()
    ForwardedModel.objects.create(userd=pk,category2=c,title2=t,img2=i,description2=d,location2=l)
    Post_Complaint.objects.filter(id=pk).delete()
    return redirect('comp')



def solution(request,pk):
    pr = ForwardedModel.objects.get(id=pk)
    cid = pr.id
    ca = pr.category2
    t = pr.title2
    d = pr.description2
    l = pr.location2
    i = pr.img2.url
    s = pr.status
    context = {'title':t,'desc':d,'id':cid,'category':ca,'image':i,'location':l,'status':s}
    return render(request, 'solution.html',{"cont":context})

def complaint_status_update(request,pk,x):
    pr = ForwardedModel.objects.get(id=pk)
    c = pr.category2
    t = pr.title2
    d = pr.description2
    l = pr.location2
    i = pr.img2.url
    if x == 0:
        ForwardedModel.objects.filter(id=pk).update(status="Resolved")
        CompletedModel.objects.create(comp_id=pk,category=c,title=t,img=i,description=d,location=l,status="Resolved")
        ForwardedModel.objects.filter(id=pk).delete()
    elif x == 1:
        ForwardedModel.objects.filter(id=pk).update(status="Not Resolved")
        CompletedModel.objects.create(comp_id=pk,category=c,title=t,img=i,description=d,location=l,status="Rejected")
        ForwardedModel.objects.filter(id=pk).delete()
    return redirect('forComp')


#pdf generator

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		notify = Notification.objects.get(id=kwargs['pk'])
		title = notify.N_title
		img = notify.N_img
		desc = notify.N_description
		date = notify.N_date
		data = {"title":title,"img":img,"desc":desc,"date":date}
		pdf = render_to_pdf('pdf.html', data)
		return HttpResponse(pdf, content_type='application/pdf')



#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		notify = Notification.objects.get(id=kwargs['pk'])
		title = notify.N_title
		img = notify.N_img
		desc = notify.N_description
		date = notify.N_date
		data = {"title":title,"img":img,"desc":desc,"date":date}
		pdf = render_to_pdf('pdf.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


#delete notification
def deleteNotification(request,pk):
    Notification.objects.filter(id=pk).delete()
    return redirect('notification')
