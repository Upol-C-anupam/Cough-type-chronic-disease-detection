from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ChangePasswordView, predict_disease
from users.forms import LoginForm
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('appointment', getattr(views, 'disease_diagnosis_view'), name='disease_diagnosis_view')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
