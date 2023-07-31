// 하단의 페이지 나누기 영역 클릭 시
// href 값 가져오기
document.querySelector(".pagination").addEventListener("click", (e) => {
  // a 동작 중지
  e.preventDefault();

  // href 가져오기
  let href = e.target.getAttribute("href");
  console.log(href);

  // href 값 actionForm 의 page value 값 대입
  document.querySelector("#page").value = href;
  // actionForm 전송
  document.querySelector("#actionForm").submit();
});

// 검색
// 찾기 버튼 클릭 시
// 검색어 입력 여부 확인하기
// 검색어가 없으면 alert()
// 검색어가 있으면 하단의 actionForm 안 keyword value 값으로 삽임
// form submit()

document.querySelector("#btn_search").addEventListener("click", (e) => {
  e.preventDefault();

  const top_keyword = document.querySelector("#top_keyword");

  if (top_keyword.value == "") {
    alert("검색어를 입력해주세요");
    top_keyword.focus();
    return;
  }
  document.querySelector("#keyword").value = top_keyword.value;
  document.querySelector("#actionForm").submit();
});

// const search = document.querySelector("#btn_search");

// search.addEventListener("click", (e) => {
//   e.preventDefault();

//   const keyword = document.querySelector("#top_keyword");

//   if (keyword.value == "") {
//     alert("검색어를 입력해주세요");
//     keyword.focus();
//     return;
//   }
//   document.querySelector("#keyword").value = keyword.value;
//   document.querySelector("#actionForm").submit();
// });
