const title = document.querySelector(".hello h1");

function handTitleClick(){
    console.log("title was click");
    title.style.color ="bule";
}

 title.addEventListener("click", handTitleClick);

