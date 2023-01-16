from django.urls import path,include
from rest_framework import routers
from django.contrib import admin
from myapp.views import myapp
from myapp.views import myappViewSet,EmployeeViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies', myappViewSet)
router.register(r'employees', EmployeeViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('my-first-app/',include("myfirstapp.urls")),
    path('',include(router.urls))

]