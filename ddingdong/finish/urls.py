from django.urls import path
from finish import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "finish"

urlpatterns = [
    path("", views.form_test, name="search"),
    path("login/", views.login, name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
