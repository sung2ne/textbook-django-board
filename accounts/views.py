from django.core.cache import cache

def send_phone_code(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        # 발송 횟수 제한 (1시간에 5회)
        cache_key = f'sms_count_{phone_number}'
        count = cache.get(cache_key, 0)

        if count >= 5:
            return JsonResponse({'error': '너무 많은 요청입니다. 1시간 후 다시 시도해주세요.'}, status=429)

        cache.set(cache_key, count + 1, 3600)  # 1시간 유지

        # ... 인증번호 발송 로직
