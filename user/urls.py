from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Login/$',Login,name="Login"),
	url(r'^Index/$',Index,name="Index"),
	url(r'^Save_Music/$',Save_Music,name="Save_Music"),
	url(r'^Get_List_Music/$',Get_List_Music,name="Get_List_Music"),
	url(r'^Delete_Music/$',Delete_Music,name="Delete_Music"),
]