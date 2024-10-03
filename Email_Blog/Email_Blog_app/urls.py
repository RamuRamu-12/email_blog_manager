from django.urls import path
from .views import generate_content, send_email

urlpatterns = [
    path('generate-content/', generate_content, name='generate_content'),
    path('send-email/', send_email, name='send_email'),
]
