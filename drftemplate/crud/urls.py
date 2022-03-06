from django.urls import path

from crud.views import RetrievePersonsAPIView, CreatePersonAPIView, RetrieveUpdateDeletePersonAPIView

urlpatterns = [
    path('list/', RetrievePersonsAPIView.as_view()),
    path('create/', CreatePersonAPIView.as_view()),
    path('<int:person_id>/', RetrieveUpdateDeletePersonAPIView.as_view()),
]