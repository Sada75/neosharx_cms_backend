from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from talks.api import NeosharxTalkViewSet
from startup_stories.api import StartupStoryViewSet
from neostories.api import NeoStoryViewSet
from projects.api import NeoProjectViewSet
from sharxathons.api import SharxathonViewSet
from robosharx.api import RoboSharxArticleViewSet
from technews.api import TechNewsViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r"talks", NeosharxTalkViewSet, basename="talks")
router.register(r"startup-stories", StartupStoryViewSet, basename="startup-stories")
router.register(r"neo-stories", NeoStoryViewSet, basename="neo-stories")
router.register(r"projects", NeoProjectViewSet, basename="projects")
router.register(r"hackathons", SharxathonViewSet, basename="hackathons")
router.register(r"robotics-news", RoboSharxArticleViewSet, basename="robotics-news")
router.register(r"tech-news", TechNewsViewSet, basename="tech-news")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("auth.urls")),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
