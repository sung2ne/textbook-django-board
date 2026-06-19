from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def pending_posts(request):
    posts = Post.objects.filter(status='pending')
    return render(request, 'posts/pending_list.html', {'posts': posts})

@staff_member_required
def approve_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.status = 'published'
    post.spam_reason = None
    post.save()
    messages.success(request, '게시글이 승인되었습니다.')
    return redirect('posts:pending')

@staff_member_required
def reject_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.status = 'rejected'
    post.save()
    messages.success(request, '게시글이 거부되었습니다.')
    return redirect('posts:pending')
