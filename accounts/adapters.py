from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        # 추가 필드 저장
        user.save()
        return user

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        # 소셜 계정에서 추가 정보 가져오기
        data = sociallogin.account.extra_data

        if sociallogin.account.provider == 'google':
            user.profile_image = data.get('picture', '')
        elif sociallogin.account.provider == 'kakao':
            kakao_account = data.get('kakao_account', {})
            profile = kakao_account.get('profile', {})
            user.profile_image = profile.get('profile_image_url', '')
        elif sociallogin.account.provider == 'naver':
            user.profile_image = data.get('profile_image', '')

        user.save()
        return user

    def pre_social_login(self, request, sociallogin):
        # 이미 같은 이메일로 가입된 계정이 있으면 연결
        if sociallogin.is_existing:
            return

        try:
            email = sociallogin.account.extra_data.get('email')
            if email:
                from django.contrib.auth import get_user_model
                User = get_user_model()
                user = User.objects.get(email=email)
                sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass
