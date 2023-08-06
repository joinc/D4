from django.urls import path
from NewsPaper import views

urlpatterns = [
    path('', views.index, name='index', ),
    # path('search/', views.SearchPosts.as_view(), name='post_search'),
    path('search/', views.search_post, name='post_search'),
    path('news/', views.PostList.as_view(), name='post_list', ),
    path('news/add/', views.PostCreateView.as_view(), name='post_create', ),
    path('news/<int:post_id>/', views.PostDetailView.as_view(), name='post_show', ),
    # path('news/<int:post_id>/', views.post_show, name='post_show', ),
    path('news/<int:post_id>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('news/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
