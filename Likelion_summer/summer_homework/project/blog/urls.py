from xml.dom.minidom import Document
from django.urls import path
from blog import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'
# 중복을 피하기 위한 url 네임스페이스
urlpatterns = [
    # /blog/
    path('', views.home, name='home'),
    path('new/', views.new, name="new"),
    path('detail/<int:post_pk>/', views.detail, name="detail"),
    path('edit/<int:post_pk>/', views.edit, name="edit"),
    path('delete/<int:post_pk>/', views.delete, name="delete"),
    path('delete_comment/<int:post_pk>/<int:comment_pk>',
         views.delete_comment, name="delete_comment"),

    # like
    path('like', views.like, name="like"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
