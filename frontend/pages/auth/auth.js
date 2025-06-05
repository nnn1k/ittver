import {apiUrl, makeRequest} from "/frontend/utils.js";

async function login_user() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await makeRequest({
        method: "POST",
        url: '/api/auth/login',
        data: {
            email,
            password
        }
    })
    if (!response){
        return
    }
    else {
        location.href = '/lk'
    }
}

window.login_user = login_user