var cards = document.querySelectorAll(".recipe-card");

cards.forEach((card,i)=>{

card.style.opacity=0;

setTimeout(()=>{

card.style.opacity=1;
card.style.transform="translateY(0)";

},i*200)

})

let favButtons = document.querySelectorAll(".fav-btn")

favButtons.forEach(btn => {

btn.addEventListener("click",()=>{

btn.classList.toggle("active")

if(btn.classList.contains("active")){

btn.innerHTML="💖"

}else{

btn.innerHTML="❤️"

}

})

})
let cards = document.querySelectorAll(".food-card")

cards.forEach((card,i)=>{

card.style.opacity="0"

setTimeout(()=>{

card.style.opacity="1"
card.style.transform="translateY(0)"

},i*150)

})