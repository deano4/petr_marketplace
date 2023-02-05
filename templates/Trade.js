let serverUrl = 'http://localhost:5000/trade';
let serverUrlHave = 'http://localhost:5000/have';
let serverUrlWant = 'http://localhost:5000/want';


function callBackend(sticker,uid) {

    const hb = document.getElementById("have-btn");
    const wb = document.getElementById("want-btn");

    document.getElementById("popup-name").innerHTML = sticker;
    document.getElementById("popup-img").src = "images/Petr Stickers/petr_" + sticker + ".jpg";

    fetch(serverUrl + '?sticker=' + sticker + '&uid=' + uid)
        .then(res => res.json())
        .then(data => {
            let temp = "";
            Object.keys(data.list_have).forEach(function(key) {
                temp += key + ": " + data.list_have[key] + "<br>";
                temp += "------------------<br>"
            });
            document.getElementById("have-list").innerHTML = temp;
            let temp2 = "";
            Object.keys(data.list_want).forEach(function(key) {
                temp2 += key + ": " + data.list_want[key] + "<br>";
                temp2 += "------------------<br>"
            });
            document.getElementById("want-list").innerHTML = temp2;
            if(data.user_have)
            {
                hb.className = "btn btn-success";
            }
            if(data.user_want)
            {
                wb.className = "btn btn-success";
            }
        })
}

function stickerPage(event,popup,uid,sticker){
    event.target.style.opacity = 0.5;
    sticker = event.target.alt;
    callBackend(sticker,uid);
    popup.style.display = 'block';
}

function haveToggle(uid,sticker,btn){
    fetch(serverUrlHave + '?sticker=' + sticker + '&uid=' + uid)
        .then(res => res.json())
        .then(data => {
            if(!data.error)
            {
                if(btn.className=="btn btn-outline-primary")
                {
                    btn.className = "btn btn-success";
                }
                else
                {
                    btn.className="btn btn-outline-primary";
                }
            }
            callBackend(sticker,uid);
        })
    
}

function wantToggle(uid,sticker,btn){
    fetch(serverUrlWant + '?sticker=' + sticker + '&uid=' + uid)
        .then(res => res.json())
        .then(data => {
            if(!data.error)
            {
                if(btn.className=="btn btn-outline-primary")
                {
                    btn.className = "btn btn-success";
                }
                else
                {
                    btn.className="btn btn-outline-primary";
                }
            }
            callBackend(sticker,uid);
        })
}

function load(){
    let params = (new URL(window.location)).searchParams;
    let uid = params.get('uid');
    console.log(uid);

    let sticker = "";

    const popup = document.getElementById("popup");
    const closeBtn = document.getElementById("closeBtn");

    const havebtn = document.getElementById("have-btn");
    const wantbtn = document.getElementById("want-btn");

    const petrs = document.querySelectorAll('.col img');
    for(let petr of petrs){
        petr.addEventListener('click', function(e){stickerPage(e,popup,uid,sticker)});
    }

    closeBtn.addEventListener('click', ()=>{
        popup.style.display = 'none';
        for(let petr of petrs){
            petr.style.opacity = 1;
        }
    });

    havebtn.addEventListener('click', function(){haveToggle(uid,sticker,havebtn)});
    wantbtn.addEventListener('click', function(){wantToggle(uid,sticker,wantbtn)});
}