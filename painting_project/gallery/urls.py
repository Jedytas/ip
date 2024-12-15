from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaintingListView.as_view(), name='painting-list'),
    path('painting/<int:pk>/', views.PaintingDetailView.as_view(), name='painting-detail'),
    path('painting/add/', views.PaintingCreateView.as_view(), name='painting-add'),
    path('painting/<int:pk>/edit/', views.PaintingUpdateView.as_view(), name='painting-edit'),
    path('painting/add/', views.PaintingCreateView.as_view(), name='painting-add'),
]
