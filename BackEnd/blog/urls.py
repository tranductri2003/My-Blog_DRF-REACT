from .views import PostList, PostDetail, PostListDetailfilter, CreatePost, EditPost, UserPostDetail, DeletePost
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/', PostList.as_view(), name='listpost'),
    #     path('category/<slug:slug>/',
    #          PostListByCategory.as_view(), name='post-list-by-category'),

    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # Post Admin URLs
    path('admin/post/create/', CreatePost.as_view(), name='createpost'),
    path('admin/post/edit/postdetail/<int:pk>/',
         UserPostDetail.as_view(), name='admindetailpost'),
    path('admin/post/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/post/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
