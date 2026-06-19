class Post(models.Model):
    STATUS_CHOICES = [
        ('published', '게시됨'),
        ('pending', '검토 대기'),
        ('rejected', '거부됨'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published')
    spam_reason = models.TextField(blank=True, null=True)  # 스팸 판정 이유
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
