let serverUrl = 'http://localhost:5000/trade';

function callBackend(sticker) {
    document.getElementById("popup-name").innerHTML = sticker;
    document.getElementById("popup-img").src = "images/Petr Stickers/petr_" + sticker + ".jpg";
    fetch(serverUrl + '?sticker=' + sticker)
        .then(res => res.json())
        .then(data => {
            let temp = "";
            Object.keys(data.users_have).forEach(function(key) {
                temp += key + ": " + data.users_have[key] + "\n";
            });
            document.getElementById("have-list").innerHTML = temp;
        })
}

function stickerPage(event,popup){
    event.target.style.opacity = 0.5;
    callBackend(event.target.alt)
    popup.style.display = 'block';
}

function load(){
    // get uid from the url window.location

    const popup = document.getElementById("popup");
    const closeBtn = document.getElementById("closeBtn");

    const petrs = document.querySelectorAll('.col img');
    for(let petr of petrs){
        petr.addEventListener('click', function(e){stickerPage(e,popup)});
    }

    closeBtn.addEventListener('click', ()=>{
        popup.style.display = 'none';
        for(let petr of petrs){
            petr.style.opacity = 1;
        }
    });
}