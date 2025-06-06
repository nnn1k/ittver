// Мобильное меню
import {makeRequest} from "/frontend/utils.js";

document.querySelector('.menu-toggle').addEventListener('click', function () {
    document.querySelector('.navbar').classList.toggle('active');
});

// Плавная прокрутка
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Обработка кнопок показа отзывов
document.querySelectorAll('.toggle-reviews').forEach(btn => {
    btn.addEventListener('click', function () {
        const reviews = this.nextElementSibling;
        reviews.classList.toggle('active');
        this.textContent = reviews.classList.contains('active') ? 'Скрыть отзывы' : 'Показать отзывы';
    });
});

async function getReviews() {
    const reviews = await makeRequest({
        url: "/api/reviews",
        method: "GET"
    })

    for (let review of reviews["1C"]) {
        let reviewElement = createReviewHTML(review);
        document.querySelector(".portfolio-reviews-one-c").appendChild(reviewElement);
    }

    for (let review of reviews["repair"]) {
        let reviewElement = createReviewHTML(review);
        document.querySelector(".portfolio-reviews-repair").appendChild(reviewElement);
    }

    for (let review of reviews["servers"]) {
        let reviewElement = createReviewHTML(review);
        document.querySelector(".portfolio-reviews-servers").appendChild(reviewElement);
    }

    return reviews.user
}

const user = await getReviews()
if (!user) {
    const addBtn = document.getElementById("add-review-btn")
    addBtn.disabled = true
    addBtn.style.backgroundColor = "red"
    addBtn.textContent = "Что бы написать отзыв, вы должны быть авторизованы"
} else {
    document.getElementById("name").value = user.name
}

function getRating() {
    const checkedStar = document.querySelector('input[name="rating"]:checked');
    return checkedStar ? parseInt(checkedStar.value) : 0;
}

document.querySelector('.rating-stars').addEventListener('change', function () {
    console.log('Выбран рейтинг:', getRating(), 'звезды');
});

async function postReview() {
    const company_name = document.getElementById('company').value
    const service = document.getElementById('service').value
    const message = document.getElementById('message').value
    const rating = getRating()
    const response = await makeRequest({
        url: "api/reviews",
        method: "POST",
        data: {
            company_name,
            service,
            message,
            rating
        }
    })
    if (!response) {
        return
    }
    alert("Отзыв отправлен")
}


function createReviewHTML(reviewData) {
    // Создаем элемент div с классом review-item
    const reviewItem = document.createElement('div');
    reviewItem.className = 'review-item';

    // Создаем заголовок отзыва
    const reviewHeader = document.createElement('div');
    reviewHeader.className = 'review-header';

    // Формируем имя пользователя (name + surname)
    const userName = `${reviewData.user?.name || ''} ${reviewData.user?.surname || ''}`.trim() || 'Анонимный пользователь';

    // Создаем блок с именем пользователя и компанией
    const userInfo = document.createElement('div');

    const clientSpan = document.createElement('span');
    clientSpan.className = 'review-client';
    clientSpan.textContent = userName;

    const companySpan = document.createElement('span');
    companySpan.className = 'review-company';
    if (reviewData.company_name) {
        companySpan.textContent = `, ${reviewData.company_name}`;
    }

    userInfo.appendChild(clientSpan);
    if (reviewData.company_name) {
        userInfo.appendChild(companySpan);
    }

    // Создаем блок с рейтингом
    const ratingDiv = document.createElement('div');
    ratingDiv.className = 'review-rating';

    // Добавляем звезды рейтинга (5 звезд, заполненные в соответствии с rating)
    for (let i = 0; i < 5; i++) {
        const starIcon = document.createElement('i');
        starIcon.className = i < reviewData.rating ? 'fas fa-star' : 'far fa-star';
        ratingDiv.appendChild(starIcon);
    }

    // Собираем заголовок
    reviewHeader.appendChild(userInfo);
    reviewHeader.appendChild(ratingDiv);

    // Создаем текст отзыва
    const reviewText = document.createElement('p');
    reviewText.className = 'review-text';
    reviewText.textContent = reviewData.message || 'Без текста';

    // Собираем весь отзыв
    reviewItem.appendChild(reviewHeader);
    reviewItem.appendChild(reviewText);

    return reviewItem;
}

async function sendContacts() {
    const name = document.getElementById("name-contact").value
    const phone = document.getElementById("phone-contact").value
    const message = document.getElementById("message-contact").value
    const email_to = "reposw0099@gmail.com"
    const response = await makeRequest({
        url: "/api/startpage/mail",
        method: "POST",
        data: {
            name,
            phone,
            message,
            email_to
        }
    })
    if (!response) {
        return
    } else {
        alert('Заявка отправлена! Мы свяжемся с вами в ближайшее время.');
    }

}

window.postReview = postReview
window.sendContacts = sendContacts