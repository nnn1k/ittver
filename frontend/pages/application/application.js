import {apiUrl, makeRequest, getUser} from "/frontend/utils.js";

const user = await getUser()


document.getElementById('name').value = user.name;
document.getElementById('phone').value = user.phone;
document.getElementById('email').value = user.email;

async function addApp(){
    const service = document.getElementById('service').value;
    const description = document.getElementById('message').value;

    const response = makeRequest({
        method: "POST",
        url: '/api/applications',
        data: {
            service, description
        }
    })
    if (response){
        alert('Заявка отправлена')
        location.href = '/lk'
    }
}

window.addApp = addApp