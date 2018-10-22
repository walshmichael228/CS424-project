from . import views
from django.contrib import admin
from Landlord.views import index
from django.urls import include, path


urlpatterns = [
    path('id_num/<int:num_id>', views.member, name = "landlord_profile"),
    path('list/', views.list1, name = 'list')
   
]