let letsgo=document.getElementById("letsgo")
let letsGO=document.getElementById("letsGO");
let lodinganimation=document.getElementById("lodinganimation")

letsgo.addEventListener("click",function(){

    letsGO.style.display="none"
    lodinganimation.style.display="flex"


    setTimeout(function() {
        window.location=("https://adarshananda.com")
       },2000);

})


