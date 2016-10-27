"""ChatServers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Student.views import sayHello
from Student.views import hours_ahead
from Student.views import showStudents
from Teacher.views import showTeachers
from templates.Jober import showJobers
from Teacher.views import returnforios
from templates.Jober import returnforios2
from PC.PaChong import showPaChongToIOS

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^showStudents/', showStudents),
    url(r'^showTeachers/', showTeachers),
    url(r'^showJobers/', showJobers),
    url(r'^returnforios/', returnforios),
    url(r'^returnforios2/$', returnforios2),
    url(r'^showPaChongToIOS/$', showPaChongToIOS)
    # url(r'^saysth/$', sayHello),
    # url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # url(r'^plus/(\d(1, 2))/$', hours_ahead)
]
