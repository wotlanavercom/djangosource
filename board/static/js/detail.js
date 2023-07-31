// delete 클래스명 이용
// 삭제 클릭 시
// a 태그 중지
// confirm("정말로 삭제하시겠습니까?")
// 확인 시 href 지정한 경로로 이동
const deleteAll = document.querySelectorAll(".delete");

deleteAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();

    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.href;
    }
  });
});

// 추천 버튼 클릭 시
// a 태그 중지
// 정말로 추천하시겠습니까? confirm 창 띄우기
// 확인 버튼 클릭 시 url 로 전송
const recommandAll = document.querySelectorAll(".recommand");

recommandAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();

    if (confirm("정말로 추천하시겠습니까?")) {
      location.href = e.target.href;
    }
  });
});
