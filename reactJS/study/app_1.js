// comst 업데이트 할 수 없는 값 
const a = 8; 
const b = 2; 

// let var 업데이트 할 수 있는 값
let myName = "AINA"; 

const veryLongVariableName = 0;

console.log(a + b);
console.log(a * b);
console.log(a / b);
console.log("hello" + myName);

myName ="nicolas";

console.log("your name is "+myName);

const amIFat = null; //null 비어있음 (자연발생하지 않음. 없다는 것을 의도적으로 표현)
let something ; //undefined 정의 되지 않음 (공간은 존재) 

console.log(something, amIFat);

//배열
const dayOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"];

console.log(dayOfWeek);
// arry에서 값 받아오기 
console.log(dayOfWeek[5]);

// array에 값 추가하기
dayOfWeek.push("sun");
console.log(dayOfWeek);


const playerName = "nicolas";
const playerPoints = 121212;
const playerHandsome = false;
const playerFat="little bit";


// 객체 (속성을 가진것을 하나로 묶고싶을때 사용함) 
const player = {
    name: "nico",
    point: 121234,
    handsome: false,
    fat: "littlebit", 
    sayHello: function(orherPersonname){
        console.log("hello!" + orherPersonname);
    }
};

console.log(player);
console.log(player .name);
//const로 선언하여도 객체 안의 속성을 변경하는 것은 가능하다. 
player.handsome = false;

player.lastName ="poteto"; // 그냥 임의로 선언하면 추가가 된다. 
player.point=65664234;
console.log(player);

//function
function sayHello(nameOfPerson, age){
    console.log("Hello! " + nameOfPerson + " and I'm " + age);
};

sayHello("nico", 10);
sayHello("dal", 23);
sayHello("lynn", 21);

function plus(firstNumber, secondNumber){
    console.log(firstNumber + secondNumber);
}
function divide(a, b){
    console.log(a / b);   
}
plus(60,5);

divide(60, 5);

console.log(player.name);
player.sayHello("lynn");









