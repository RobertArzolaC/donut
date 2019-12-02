from django.urls import path
from .views import WorkSpaceView, Neo4jQueryView

urlpatterns = [
    path('set-graph', WorkSpaceView.as_view()),
    path('get-graph', Neo4jQueryView.as_view()),
]
