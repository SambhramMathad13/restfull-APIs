from django.contrib import admin
from django.urls import path
from rest.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud/',Studapi.as_view()),
    path('stud/<int:id>',Studapi.as_view()),



    # for function based view
    # path('stud/',Studapi),
    # path('stud/<int:id>',Studapi),
]
