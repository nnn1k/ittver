export const apiUrl = window.location.protocol + '//' + window.location.host;

export async function makeRequest(request) {
    try {
        const response = await fetch(
            request.url,
            {
                method: request.method,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(request.data)
            }
        );

        if (response.ok) {
            const data = await response.json();
            console.log(data);
            return data;
        } else if (response.status === 401) {
            location.href = '/auth';
            return Promise.reject(new Error('Unauthorized')); // Чтобы можно было отловить
        } else if (response.status === 422){
            alert('Форма заполнена неверно')
        } else if (response.status >= 400 && response.status < 500) {
            const errorData = await response.json();
            console.log(errorData);
            alert(errorData.detail)
            return Promise.reject(new Error(errorData.detail || 'Client Error'));
        } else if (response.status === 500) {
            console.error('Ошибка 500: Внутренняя ошибка сервера.');
            return Promise.reject(new Error('Internal Server Error'));
        }
    } catch (error) {
        console.error('Ошибка сети или другая ошибка:', error);
        return Promise.reject(error);
    }
}

export async function getUser(){
    const response = await makeRequest({
        method: "GET",
        url: '/api/users/me'
    })
    return response.user
}