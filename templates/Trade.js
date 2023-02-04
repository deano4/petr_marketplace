let serverUrl = 'https://0394-169-234-78-124.ngrok.io/trade';

function callBackend(sticker) {
    fetch(serverUrl + '?sticker=' + sticker)
        .then(res => res.json())
        .then(data => {
            console.log(data.users_have)
        })
}

function stickerPage(event,popup){
    event.target.style.opacity = 0.5;
    popup.style.display = 'block';
    callBackend(event.target.alt)
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