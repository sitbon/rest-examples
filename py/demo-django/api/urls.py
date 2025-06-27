from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, NoteViewSet, UserViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
