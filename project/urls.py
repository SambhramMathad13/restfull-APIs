from django.contrib import admin
from django.urls import path,include
from rest.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
router=DefaultRouter()
router.register('studapi',StudModelViewset,basename="student")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refreshtoken/',TokenRefreshView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view()),
    # path('stud/',StudapiLC.as_view()),
    # path('stud/<int:pk>',StudapiRUD.as_view()),



    # for function based view
    # path('stud/',Studapi),
    # path('stud/<int:id>',Studapi),
]
