from allauth.socialaccount.signals import social_account_added, social_account_removed
from django.dispatch import receiver

@receiver(social_account_added)
def social_account_added_handler(request, sociallogin, **kwargs):
    messages.success(request, f'{sociallogin.account.provider} 계정이 연결되었습니다.')

@receiver(social_account_removed)
def social_account_removed_handler(request, socialaccount, **kwargs):
    messages.info(request, f'{socialaccount.provider} 계정 연결이 해제되었습니다.')
