from django.urls import path
from .views import HomePageView, MovieDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('movie/<int:movie_id>/', MovieDetailView.as_view(), name='movie_detail'),
]
