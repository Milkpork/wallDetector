from django.urls import path
import climbDetector.views as climb_views

urlpatterns = [
    path('process/', climb_views.imgFunc)
]
