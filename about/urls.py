from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.about_me, name='about'),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
]