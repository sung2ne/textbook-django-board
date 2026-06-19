def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            # 게시글 작성자에게 알림 (본인 댓글 제외)
            if post.author != request.user and post.author.email:
                send_mail(
                    subject=f'[게시판] "{post.title}" 글에 새 댓글이 달렸습니다',
                    message=f'''
{request.user.username}님이 댓글을 남겼습니다.

댓글 내용: {comment.content[:100]}...

게시글 확인하기: {request.build_absolute_uri(reverse('posts:detail', args=[post.id]))}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[post.author.email],
                    fail_silently=True,  # 메일 발송 실패해도 댓글은 저장
                )

            return redirect('posts:detail', post_id=post.id)

    return redirect('posts:detail', post_id=post.id)
