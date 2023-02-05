let serverurl_login = 'http://localhost:5000/login'
let serverurl_sign_up = 'http://localhost:5000/sign-up'

//the function that adds some 'spirit' to the program 
function click_image_function() {
    var x = document.getElementById('spirit_message');
    x.style.display = 'block'
    x.style.animation = 'hideAnimation 0s ease-in 3s';
}

//the function that switches the content when pressing the 'login' button
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

//the function that switches the content when pressing the 'sign_up' button
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


//the function that approves the 'login' info
function login(event) {
    user_name = document.getElementById('username').value;
    password = document.getElementById('password').value;
    fetch(serverurl_login + '?username=' + user_name + '&password=' + password)
        .then(res => res.json())
        .then(data => {
            console.log(data.error);
            if(!data.error) {
                let logged_in_user = data.uid;
                window.location = './TradePage.html?uid=' + logged_in_user;
            }
            else
            {
                document.getElementById('username').value = "";
                document.getElementById('password').value = "";
                document.getElementById('alert').style.display = 'block';
                //clear text boxes, raise an alert pop-up, 
            }
    })
}

//the function that approves the 'sign_up' info
function sign_up(event) {
    user_name = document.getElementById('username').value;
    password = document.getElementById('password').value;
    socials = document.getElementById('socials').value;
    fetch(serverurl_sign_up + '?username=' + user_name + '&password=' + password + '&socials=' + socials)
        .then(res => res.json())
        .then(data => {
            console.log(data.error);
            if(!data.error) {
                let logged_in_user = data.uid;
                window.location = './TradePage.html?uid=' + logged_in_user;
            }
            else
            {
                document.getElementById('username').value = "";
                document.getElementById('password').value = "";
                document.getElementById('socials').value = "";
                document.getElementById('alert').style.display = 'block';
            }
    })
}



