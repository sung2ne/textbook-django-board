from solapi import SolapiMessageService

class KoreaSMSService:
    def __init__(self):
        self.client = SolapiMessageService(
            api_key=settings.SOLAPI_API_KEY,
            api_secret=settings.SOLAPI_API_SECRET
        )

    def send_sms(self, to, message):
        """SMS를 발송합니다."""
        self.client.send_one({
            'to': to.replace('-', ''),
            'from': settings.SOLAPI_SENDER_NUMBER,
            'text': message
        })

    def send_verification_code(self, phone_number):
        code = str(random.randint(100000, 999999))
        message = f'[게시판] 인증번호는 {code}입니다.'
        self.send_sms(phone_number, message)
        return code
