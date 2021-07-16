from django.urls import path
from Docs import views

app_name="Docs"

urlpatterns=[
path('',views.MainView,name="main"),
path('upload/',views.file_upload_view,name="upload")
]
