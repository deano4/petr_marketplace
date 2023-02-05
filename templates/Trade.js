let serverUrl = 'http://localhost:5000/trade';

function callBackend(sticker,uid) {
    document.getElementById("popup-name").innerHTML = sticker;
    document.getElementById("popup-img").src = "images/Petr Stickers/petr_" + sticker + ".jpg";
    fetch(serverUrl + '?sticker=' + sticker + '&uid=' + uid)
        .then(res => res.json())
        .then(data => {
            let temp = "";
            Object.keys(data.users_have).forEach(function(key) {
                temp += key + ": " + data.users_have[key] + "<br>";
                temp += "------------------<br>"
            });
            document.getElementById("have-list").innerHTML = temp;
            let temp2 = "";
            Object.keys(data.users_want).forEach(function(key) {
                temp2 += key + ": " + data.users_want[key] + "<br>";
                temp2 += "------------------<br>"
            });
            document.getElementById("want-list").innerHTML = temp2;
        })
}

function stickerPage(event,popup,uid){
    event.target.style.opacity = 0.5;
    callBackend(event.target.alt,uid)
    popup.style.display = 'block';
}

function haveToggle(event,uid){}

function wantToggle(event,uid){}

function load(){
    let params = (new URL(window.location)).searchParams;
    let uid = params.get('uid');
    console.log(uid);

    const popup = document.getElementById("popup");
    const closeBtn = document.getElementById("closeBtn");

    const havebtn = document.getElementById("have-btn");
    const wantbtn = document.getElementById("want-btn");

    havebtn.addEventListener('click', function(e){haveToggle(e,uid)});
    wantbtn.addEventListener('click', function(e){haveToggle(e,uid)});

    const petrs = document.querySelectorAll('.col img');
    for(let petr of petrs){
        petr.addEventListener('click', function(e){stickerPage(e,popup,uid)});
    }

    closeBtn.addEventListener('click', ()=>{
        popup.style.display = 'none';
        for(let petr of petrs){
            petr.style.opacity = 1;
        }
    });
}