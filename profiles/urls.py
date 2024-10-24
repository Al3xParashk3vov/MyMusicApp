from profiles import views
from django.urls import path

urlpatterns = [
    path('details/', views.ProfileDetailView.as_view(), name='profile-details'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]