import {apiUrl, makeRequest} from "/frontend/utils.js";

async function register_user() {
    const name = document.getElementById('firstName').value;
    const surname = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirm_password = document.getElementById('confirmPassword').value;
    const phone = document.getElementById('phone').value;

    const response = await makeRequest({
        method: "POST",
        url: '/api/auth/register',
        data: {
            name,
            surname,
            email,
            password,
            confirm_password,
            phone
        }
    })
    if (!response){
        return
    }
    else {
        location.href = '/lk'
    }
}

window.register_user = register_user