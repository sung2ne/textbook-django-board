class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def summarize(self, content, max_length=100):
        # ... 기존 코드

    def check_spam(self, title, content):
        """게시글이 스팸인지 검사합니다."""
        prompt = f"""다음 게시글이 스팸인지 분석해주세요.

        제목: {title}
        내용: {content}

        다음 기준으로 판단해주세요:
        1. 광고성 내용 (상품 홍보, 링크 유도 등)
        2. 욕설 또는 비방
        3. 도박, 불법 사이트 홍보
        4. 무의미한 반복 텍스트

        결과를 JSON 형식으로 응답해주세요:
        {{"is_spam": true/false, "reason": "판단 이유", "confidence": 0.0~1.0}}
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 스팸 탐지 전문가입니다. JSON 형식으로만 응답하세요."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0
        )

        import json
        result = json.loads(response.choices[0].message.content)
        return result
