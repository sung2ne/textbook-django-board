from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from .forms import PostCreateForm

# 게시글 등록
def create_post(request):
    form = PostCreateForm()
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, '게시글이 등록되었습니다.')
            return redirect("posts:read", post_id=post.id)
        else:
            messages.error(request, '게시글 등록에 실패했습니다.')
    
    return render(request, 'posts/create.html', {'form': form})

# 게시글 보기
def get_post(request, post_id):
    return HttpResponse('게시글 보기')

# 게시글 수정
def update_post(request, post_id):
    return HttpResponse('게시글 수정')

# 게시글 삭제
def delete_post(request, post_id):
    return HttpResponse('게시글 삭제')

# 게시글 목록
def get_posts(request):
    return HttpResponse('게시글 목록')
