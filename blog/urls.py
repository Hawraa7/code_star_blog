from . import views
from django.urls import path
from .views import PostList, event_detail, post_detail 
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("event/<int:event_id>/", event_detail, name="event_detail"),
    path("post/<slug:slug>/", post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
]
