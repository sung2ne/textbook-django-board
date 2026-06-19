urlpatterns = [
    # ... 기존 URL
    path('send-phone-code/', views.send_phone_code, name='send_phone_code'),
    path('verify-phone-code/', views.verify_phone_code, name='verify_phone_code'),
]
