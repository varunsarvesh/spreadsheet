from django.urls import path
from upload import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.xlapp, name='xlapp'),
    path('upload/', views.upload, name='upload'),
    path('view/', views.view, name='view'),
    path('uploading/', views.uploading, name='uploading'),

]
