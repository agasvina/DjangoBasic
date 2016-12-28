from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


from django.views.generic.base import TemplateView
from ang.views import AngularTemplateView

from accounts.views import (
    login_view,
    register_view,
    logout_view,
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
 

 	url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    url(r'^login/', login_view, name='login'),
    url(r'^register/', register_view, name='register'),
    url(r'^logout/', logout_view, name='logout'),

    url(r'^api/user/', include('accounts.api.urls', namespace='user-api')),
    url(r'^api/todo/', include('todos.api.urls', namespace='todo-api')),
    url(r'^api/kaggle/', include('kaggle.api.urls', namespace='kaggle-api')),

    #Serving angular template:
    url(r'^api/templates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$',  AngularTemplateView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'', TemplateView.as_view(template_name='ang/index.html')),

]