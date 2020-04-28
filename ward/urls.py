"""ward URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from user import views
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('',views.index, name='index'),
    path('register',views.register, name="register"),
    path('user_page',views.user_page, name="user_page"),
    path('post_comp',views.post_comp, name="post_comp"),
    path('comp',views.comp,name="comp"),
    path('all_comp',views.all_comp,name="all_comp"),
    path('admin',views.admin,name="admin"),
    path('notification',views.notification,name="notification"),
    path('notify',views.notify,name="notify"),
    path('forComp',views.forComp,name="forComp"),
    path('resolved_complaints',views.resolved_complaints,name="resolved_complaints"),
    path('rejected_complaints',views.rejected_complaints,name="rejected_complaints"),
    
    path('send_email/(?P<pk>\d+)/$',views.send_email, name="send_email"),
    path('solution/(?P<pk>\d+)/$',views.solution,name="solution"),
    path('<int:pk><int:x>/',views.complaint_status_update, name="complaint_status_update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
