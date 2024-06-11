from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate


urlpatterns = [
     path('', PostList.as_view()),
     path('<int:pk>', PostDetail.as_view()),
     path('search', PostSearch.as_view()),
     path('create/', PostCreate.as_view(), name='post_create'),
     path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
]
