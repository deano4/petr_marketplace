const login_button = document.querySelector('#login_button');
const sign_up_button = document.querySelector('#sign_up_button');
const submit_button = document.querySelector('#submit_button');
const element = document.getElementById("myBtn");


sign_up.addEventListener("click", change_to_sign_in);
login_button.addEventListener("click", change_to_log_in);
submit_button.addEventListener("click", login(e));

function change_to_sign_up() {
    document.getElementById("socials_label").style.display = "";
    document.getElementById("socials").style.display = "";
}

function change_to_log_in() {
    document.getElementById("socials_label").style.display = "none";
    document.getElementById("socials").style.display = "none";
}

element.addEventListener("click", myFunction);

function myFunction() {
  document.getElementById("myBtn").innerHTML = "Hello World";
}

/*
function login(event) {
    event.preventDefault();
    fetch('serverulr/login?username=document.getEmeply()p&pw').then(res => res.json()).then(response => {
        if not logogedinuser in return
        let logogedinuser = response.uid
        window.location = './TradePage.html?uid=' + logogedinuser
    })
}
*/


