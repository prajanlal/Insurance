function goLogin(){
    window.location.href = "login.html";
}

function toggleFAQ(element){
    let p = element.querySelector("p");
    p.style.display = p.style.display === "block" ? "none" : "block";
}