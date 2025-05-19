from django.urls import path
from . import views

urlpatterns = [
    path('detector', views.show_detector, name='detector'),
    path('report', views.show_report, name='report'),
    path('save-suspicious-logs', views.save_suspicious_logs, name='save_suspicious_logs'),
    path('get-suspicious-logs', views.get_suspicious_logs, name='get_suspicious_logs'),
]
