let serverUrl = 'https://0394-169-234-78-124.ngrok.io/trade';

function callBackend(sticker) {
    fetch(serverUrl + '?sticker=' + sticker)
        .then(res => res.json())
        .then(data => {
            console.log(data.users_have)
        })
}

function popUp(event){
    event.target.style.opacity = 0.5;
    callBackend(event.target.alt)
}

function load(){
    // get uid from the url window.location

    const petrs = document.querySelectorAll('.col img');
    for(let petr of petrs){
        petr.addEventListener('click', function(e){popUp(e)});
    }
}