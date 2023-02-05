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
    z2.style.textAlign =  'center';

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
    z.style.textAlign =  'center';
}
}

function login(event) {
    user_name = document.getElementById('username').value;
    password = document.getElementById('password').value;
    console.log(user_name, password)
    fetch(serverurl_login + '?username=' + user_name + '&password=' + password)
        .then(res => res.json())
        .then(data => {
            console.log(data.error);
            if(!data.error) {
                let logged_in_user = data.uid;
                window.location = './TradePage.html?uid=' + logged_in_user;
            }
    })
}

/*
function sign_up(event) {
    socials = document.getElementById('socials').value;
    user_name = document.getElementById('username').value;
    password = document.getElementById('password').value;
    fetch(serverurl_sign_up).then(res => res.json()).then(response => {
        if not logogedinuser in return
        let logogedinuser = response.uid
        window.location = './TradePage.html?uid=' + logogedinuser
    })
}
*/



