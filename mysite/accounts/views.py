from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm

# 회원가입
def register_account(request):
    if request.user.is_authenticated:
        return redirect('auth:profile')

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
                first_name=form.cleaned_data["first_name"],
                email=form.cleaned_data["email"]
            )
            user.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('auth:login')
        else:
            messages.error(request, '회원가입에 실패했습니다.')

    return render(request, 'accounts/register.html', {'form': form, 'message_class': 'col-4 mx-auto'})

# 로그인
def login_account(request):
    if request.user.is_authenticated:
        return redirect('auth:profile')
    
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            # 로그인 실패
            if user is None:
                messages.error(request, '아이디 또는 비밀번호가 일치하지 않습니다.')
                return redirect('auth:login')

            # 로그인 성공
            login(request, user)
            return redirect('auth:profile')
        else:
            messages.error(request, '아이디 또는 비밀번호를 입력해주세요.')

    return render(request, 'accounts/login.html', {'form': form, 'message_class': 'col-4 mx-auto'})

# 로그아웃
def logout_account(request):
    return HttpResponse('로그아웃')

# 프로필 보기
def get_profile(request):
    return HttpResponse('프로필 보기')

# 프로필 수정
def update_profile(request):
    return HttpResponse('프로필 수정')

# 비밀번호 수정
def update_password(request):
    return HttpResponse('비밀번호 수정')

# 아이디 찾기
def find_username(request):
    return HttpResponse('아이디 찾기')

# 비밀번호 초기화
def reset_password(request):
    return HttpResponse('비밀번호 초기화')

# 사용자 탈퇴
def delete_account(request):
    return HttpResponse('사용자 탈퇴')
