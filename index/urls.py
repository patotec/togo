from django.urls import path
from . import views

app_name = 'indexurl'
urlpatterns = [
	path('',  views.myindex ,name='index'),
    path('send-email',  views.send ,name='profile'),
	
 ]