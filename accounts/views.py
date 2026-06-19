from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # 이메일 인증 전까지 비활성화
            user.save()

            # 인증 토큰 생성 및 메일 발송
            token = user.generate_email_token()
            verify_url = request.build_absolute_uri(
                reverse('accounts:verify_email', args=[token])
            )

            send_mail(
                subject='[게시판] 이메일 인증을 완료해주세요',
                message=f'''
안녕하세요, {user.username}님!

아래 링크를 클릭하여 이메일 인증을 완료해주세요.

{verify_url}

감사합니다.
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

            messages.info(request, '인증 메일이 발송되었습니다. 이메일을 확인해주세요.')
            return redirect('accounts:login')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

def verify_email(request, token):
    try:
        user = User.objects.get(email_token=token)
        user.is_active = True
        user.email_verified = True
        user.email_token = None
        user.save()
        messages.success(request, '이메일 인증이 완료되었습니다.')
    except User.DoesNotExist:
        messages.error(request, '유효하지 않은 인증 링크입니다.')

    return redirect('accounts:login')
