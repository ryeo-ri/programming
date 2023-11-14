/*
const loginForm = document.getElementById("login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("Button");
*/
const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form Button");

function onLoginBtnClick(){
    const username = loginInput.value;
    console.log(username);
}

loginButton.addEventListener("click",onLoginBtnClick);