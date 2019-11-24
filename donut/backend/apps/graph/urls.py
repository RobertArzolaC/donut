from django.urls import path
from .views import WorkSpaceView 

urlpatterns = [
    path('set-graph', WorkSpaceView.as_view()),
]
