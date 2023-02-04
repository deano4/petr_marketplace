const petrs = document.querySelectorAll('.col');
let serverUrl = '';

function popUp(event){
    event.target.style.opacity = 0.5;
}

for(let petr of petrs){
    petr.addEventListener('click', function(e){popUp(e)});
}