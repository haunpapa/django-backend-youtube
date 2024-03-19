from django.urls import path
from .views import VideoList, VideoDetail


# api/v1/video/

urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
    # path('<int:video_id>/', VideoDetail.as_view(), name='video-detail')
]