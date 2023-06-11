from django.contrib import admin
from django.urls import path

from apps.common.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SignUpView.as_view(), name='home'),
]
