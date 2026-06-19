from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_verification_email_task(user_email, username, verify_url):
    send_mail(
        subject='[게시판] 이메일 인증을 완료해주세요',
        message=f'''
안녕하세요, {username}님!
아래 링크를 클릭하여 이메일 인증을 완료해주세요.
{verify_url}
        ''',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
    )

# views.py에서 사용
from .tasks import send_verification_email_task

def signup(request):
    # ... 회원가입 처리
    send_verification_email_task.delay(user.email, user.username, verify_url)
