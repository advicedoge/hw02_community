from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls')),
    path('index.html', include('posts.urls')),
    path('group/<slug:slug>/', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls)
]
