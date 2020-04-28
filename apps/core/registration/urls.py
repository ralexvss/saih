from django.urls import path
from .views import RegisterCreateView, ProfileUpdate, ProfileList, ProfileDetail, ProfileEmailUpdate

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/list/', ProfileList.as_view(), name='profile_list'),
    path('profile/detail/<username>/',
         ProfileDetail.as_view(), name='profile_detail'),
    path('profile/email/', ProfileEmailUpdate.as_view(), name='profile_email'),
]
