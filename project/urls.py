from django.contrib import admin
from django.urls import path,include
from rest.views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('studapi',StudModelViewset,basename="student")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('stud/',StudapiLC.as_view()),
    # path('stud/<int:pk>',StudapiRUD.as_view()),



    # for function based view
    # path('stud/',Studapi),
    # path('stud/<int:id>',Studapi),
]
