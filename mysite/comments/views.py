from django.http import JsonResponse

# 댓글 등록
def create_comment(request):
    return JsonResponse({'message': '댓글 등록'})

# 댓글 수정
def update_comment(request, comment_id):
    return JsonResponse({'message': '댓글 수정'})

# 댓글 삭제
def delete_comment(request, comment_id):
    return JsonResponse({'message': '댓글 삭제'})
