from django.contrib import admin
from django.urls import path, include
from .views import signupview, loginview, listview, detailview, CreateClass, logoutview, evaluationview
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import debug_toolbar
from .views import emailfunc

urlpatterns = [
	path('admin/', admin.site.urls),
	path('signup/', signupview, name="signup"),
	path('login/', loginview, name="login"),
	path('list/', listview, name="list"),
	path('detail/<int:pk>', detailview, name="detail"),
	path('create/', CreateClass.as_view(), name="create"),
	path('logout/', logoutview, name="logout"),
	path('evaluation/<int:pk>', evaluationview, name="evaluation"),
	path('accounts/', include('django.contrib.auth.urls')),
	path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
	path('email', emailfunc),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]