from django.conf.urls import include, url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from communities.api_views import CommunityView
from users.api_views import UserView, schema_view

router = routers.DefaultRouter()
router.register(r'communities', CommunityView)


urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^jwt/get-token/', obtain_jwt_token),
    url(r'^jwt/refresh/', refresh_jwt_token),
    url(r'^profile/$', UserView.as_view()),
    url(r'^docs/$', schema_view),
    url(r'^', include(router.urls, namespace='restapi')),
]
