from django.contrib import admin
from django.urls import path
# from .views import *
from .views import *
urlpatterns=[
    # path('', show, name='show')
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', student_detail),
    path('stuinfo/', student_list),
]
