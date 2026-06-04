from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, RegisterView, LoginView, LogoutView

router = DefaultRouter()
router.register('notes', NoteViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]

urlpatterns += router.urls