from django.urls import path
from form.views import index, custom_404

urlpatterns = [path('', index, name='home')]
handler404 = custom_404
