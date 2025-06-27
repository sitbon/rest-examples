from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, NoteViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = router.urls
