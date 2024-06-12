from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete


urlpatterns = [
     path('', PostList.as_view()),
     path('<int:pk>', PostDetail.as_view()),
     path('news/search', PostSearch.as_view()),
     path('news/create/', PostCreate.as_view(), name='post_create'),
     path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
     path('news/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
     path('article/create/', PostCreate.as_view(), name='post_create'),
     path('article/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
     path('article/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
