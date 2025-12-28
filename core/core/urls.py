from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from talks.api import NeosharxTalkViewSet
from startup_stories.api import StartupStoryViewSet
from neostories.api import NeoStoryViewSet
from projects.api import NeoProjectViewSet
from sharxathons.api import SharxathonViewSet





router = DefaultRouter()
router.register(r"talks", NeosharxTalkViewSet, basename="talks")
router.register(r"startup-stories", StartupStoryViewSet, basename="startup-stories")
router.register(r"neo-stories", NeoStoryViewSet, basename="neo-stories")
router.register(r"projects", NeoProjectViewSet, basename="projects")
router.register(r"hackathons", SharxathonViewSet, basename="hackathons")



urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
