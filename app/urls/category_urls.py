from django.urls import path
from .. import views

urlpatterns = [
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
]