"""implement API urls here."""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from flightApi.views import user_auth, api_status

# pylint: disable=invalid-name
welcome_message = api_status.ApiStatusViewSet.as_view({
    'get': 'retrieve'
})

user_signup = user_auth.UserAuthViewSet.as_view({
    'post': 'create',
})


urlpatterns = format_suffix_patterns([
    url(r'^$', welcome_message, name='welcome_message'),
    url(r'^api/v1/auth/signup/$', user_signup, name='user_signup'),
])
