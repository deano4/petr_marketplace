let serverurl_login = 'http://localhost:5000/login'
let serverurl_sign_up = 'http://localhost:5000/sign_up'

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

user_name = document.getElementById('username').textContent;
password = document.getElementById('password').textContent;
socials = document.getElementById('socials').textContent;

function login(event) {
    fetch(serverurl_login + '?username=' + user_name + '&password=' + password)
        .then(res => res.json())
        .then(data => {
            if(!data.error) {
                console.log('got here!');
                let logged_in_user = data.uid;
                window.location = './TradePage.html?uid=' + logged_in_user;
            }
    })
}

/*
function sign_up(event) {
    fetch(serverurl_sign_up).then(res => res.json()).then(response => {
        if not logogedinuser in return
        let logogedinuser = response.uid
        window.location = './TradePage.html?uid=' + logogedinuser
    })
}
*/



