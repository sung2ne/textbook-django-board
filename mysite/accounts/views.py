from django.http import HttpResponse

# 회원가입
def register_account(request):
    return HttpResponse('회원가입')

# 로그인
def login_account(request):
    return HttpResponse('로그인')

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
