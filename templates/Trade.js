const petrs = document.querySelectorAll('.col');

function popUp(event){
    console.log(event.target.alt);
}

for(let petr of petrs){
    petr.addEventListener('click', function(e){popUp(e)});
}