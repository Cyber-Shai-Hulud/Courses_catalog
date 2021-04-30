from rest_framework import routers
from .api import CoursesViewSet

# Url routing for api
router = routers.DefaultRouter()
router.register('api/courses', CoursesViewSet, 'courses')

urlpatterns = router.urls
