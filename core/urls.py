from django.urls import include, path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:name>/', views.category, name='category_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:article_id>/add_comment/', views.add_comment, name='add_comment'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]