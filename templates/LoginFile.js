
const submit_button = document.querySelector('#submit_button');

button.addEventListener('click', function (e) {
    container.style.backgroundColor = makeRandColor();
    e.stopPropagation(); //Stops bubbling
})
container.addEventListener('click', function () {
    container.classList.toggle('hide');
})

const makeRandColor = () => {
    const r = Math.floor(Math.random() * 255);
    const g = Math.floor(Math.random() * 255);
    const b = Math.floor(Math.random() * 255);
    return `rgb(${r}, ${g}, ${b})`;

}



function login(event) {
    event.preventDefault();
    fetch('serverulr/login?username=document.getEmeply()p&pw').then(res => res.json()).then(response => {
        if not logogedinuser in return
        let logogedinuser = response.uid
        window.location = './TradePage.html?uid=' + logogedinuser
    })
}

