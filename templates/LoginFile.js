
function login_function() {
var x = document.getElementById('socials');
var y = document.getElementById('socials_label');
var z = document.getElementById('submit')
var z2 = document.getElementById('submit2')
if (x.style.display == 'block' && y.style.display === 'block') {
    x.style.display = 'none';
    y.style.display = 'none';
    z.style.display = 'none';
    z2.style.display = 'block';
    z2.style.textAlign =  center;

}
}

function sign_up_function() {
var x = document.getElementById('socials');
var y = document.getElementById('socials_label');
var z = document.getElementById('submit')
var z2 = document.getElementById('submit2')
if (x.style.display == 'none' && y.style.display === 'none') {
    x.style.display = 'block';
    y.style.display = 'block';
    z.style.display = 'block';
    z2.style.display = 'none';
    z.style.textAlign =  center;
}
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


