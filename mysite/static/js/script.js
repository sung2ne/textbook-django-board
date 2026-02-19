// 공통 자바스크립트

// 삭제 확인
function confirmDelete() {
    return confirm('정말 삭제하시겠습니까?');
}

// 폼 유효성 검사
function validateForm(form) {
    const title = form.querySelector('[name="title"]');
    const content = form.querySelector('[name="content"]');

    if (title && title.value.trim() === '') {
        alert('제목을 입력하세요.');
        title.focus();
        return false;
    }

    if (content && content.value.trim() === '') {
        alert('내용을 입력하세요.');
        content.focus();
        return false;
    }

    return true;
}

// 페이지 로드 완료 시 실행
document.addEventListener('DOMContentLoaded', function() {
    console.log('페이지 로드 완료');
});
