from django.urls import path
from . import views
from .views import SignUpView
# from .views import (
#     MemoCreateView,
#     MemoListView,
#     MemoDetailView,
#     MemoUpdateView,
#     MemoDeleteView,
# )

urlpatterns = [
    path('', views.MemoListView.as_view(), name='memo_list'),
    path('create/', views.MemoCreateView.as_view(), name='memo_create'),
    path('<int:pk>/update/', views.MemoUpdateView.as_view(), name='memo_update'),
    path('<int:pk>/delete/', views.MemoDeleteView.as_view(), name='memo_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
]