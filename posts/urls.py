urlpatterns = [
    # ... 기존 URL 패턴
    path('pending/', views.pending_posts, name='pending'),
    path('<int:post_id>/approve/', views.approve_post, name='approve'),
    path('<int:post_id>/reject/', views.reject_post, name='reject'),
]
