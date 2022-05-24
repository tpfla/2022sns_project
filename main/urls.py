from django.urls import path
from pip import main
from .views import *

app_name = "sns_project"
urlpatterns = [
    path('', main, name="showmain"),
    path('<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('delete/<str:id>', delete, name="delete"),
]
