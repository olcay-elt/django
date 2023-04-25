from django.urls import path
from .views import *
urlpatterns = [
    #  path('/',cohortFS),
    path('FS/',cohortFS),
    path('AWS/',cohortAWS),

]