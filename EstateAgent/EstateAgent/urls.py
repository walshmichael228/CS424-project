
from django.contrib import admin
from EstateAgent.views import index
from django.urls import include, path

urlpatterns = [
    path('admin/',admin.site.urls),
    path('landlord/', include('Landlord.urls'))
]



  


    
