import {getUser, makeRequest} from "/frontend/utils.js";

document.addEventListener('DOMContentLoaded', function () {
    // Элементы меню
    const newTicketBtn = document.querySelector('.quick-actions .btn.primary');
    const reportBtn = document.querySelector('.quick-actions .btn.secondary');
    const myTicketsBtn = document.querySelector('.menu-section li:nth-child(2) a');

    // Модальные окна
    const modals = {
        newTicket: document.getElementById('newTicketModal'),
        report: document.getElementById('reportModal'),
        myTickets: document.getElementById('myTicketsModal')
    };

    // Инициализация модальных окон
    function initModals() {
        // Закрытие по клику на крестик
        document.querySelectorAll('.close-modal').forEach(btn => {
            btn.addEventListener('click', closeAllModals);
        });

        // Закрытие по клику вне окна
        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('click', function (e) {
                if (e.target === this) closeAllModals();
            });
        });

        // Закрытие по кнопке "Отмена"
        document.querySelectorAll('.close-modal-btn').forEach(btn => {
            btn.addEventListener('click', closeAllModals);
        });

        // Обработчики форм
        document.getElementById('ticketForm')?.addEventListener('submit', function (e) {
            e.preventDefault();
            alert('Заявка успешно создана!');
            this.reset();
            closeAllModals();
        });

        document.getElementById('reportForm')?.addEventListener('submit', function (e) {
            e.preventDefault();
            alert('Отчет готовится и будет отправлен вам на почту!');
            this.reset();
            closeAllModals();
        });
    }

    // Функция открытия модального окна
    function openModal(modal) {
        closeAllModals();
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';

        // Загружаем данные, если это окно "Мои заявки"
        if (modal === modals.myTickets) {
            loadMyTickets();
        }
    }

    // Функция закрытия всех модальных окон
    function closeAllModals() {
        Object.values(modals).forEach(modal => {
            modal.style.display = 'none';
        });
        document.body.style.overflow = 'auto';
    }

    // Загрузка данных для "Мои заявки"
    function loadMyTickets() {
        const ticketsList = document.querySelector('#myTicketsModal .tickets-list');
        if (!ticketsList) return;
        console.log(user.applications[0].status);
        ticketsList.innerHTML = user.applications.map(ticket => `
            <div class="ticket-item">
                <div class="ticket-info">
                    <h3>#${ticket.id} - ${ticket.description}</h3>
                    <div class="ticket-meta">
                        <span>${ticket.created_at}</span>
                        <span class="status ${ticket.status === 'in_progress' ? 'in_progress' : 'completed'}">
                            ${ticket.status === 'active' ? 'Завершено' : 'В работе'}
                        </span>
                    </div>
                </div>
                <div class="ticket-actions">
                    <a href="#" class="btn small">Подробнее</a>
                </div>
            </div>
        `).join('');
    }

    // Назначение обработчиков кнопкам
    if (newTicketBtn) {
        newTicketBtn.addEventListener('click', function (e) {
            e.preventDefault();
            openModal(modals.newTicket);
        });
    }

    if (reportBtn) {
        reportBtn.addEventListener('click', function (e) {
            e.preventDefault();
            openModal(modals.report);
        });
    }

    if (myTicketsBtn) {
        myTicketsBtn.addEventListener('click', function (e) {
            e.preventDefault();
            openModal(modals.myTickets);
        });
    }

    // Инициализация
    initModals();
});

const user = await getUser()
document.getElementById('user-name').textContent = `${user.name} ${user.surname}`
document.getElementById('count-in-progress').textContent = user.applications.length
for (let app of user.applications) {
    let applTable = document.getElementById('applications-table')
    applTable.innerHTML += `
  <tr>
        <td>${app.id}</td>
        <td>${getServiceName(app.service)}</td>
        <td><span class="status-badge status-${app.status}">${getStatusText(app.status)}</span></td>
        <td>${formatDate(app.created_at)}</td>
  </tr>
  `
}

function getServiceName(service) {
    const services = {
        'repair': 'Ремонт техники',
        '1C': 'Настройка 1С',
        'service': 'Обслуживание',
        'other': 'Другое'
    };
    return services[service] || service; // Возвращает оригинальное значение, если нет в списке
}

function getStatusText(status) {
    const statuses = {
        'active': 'В работе',
        'completed': 'Завершено',
        'in_progress': 'Ожидание',
        'cancel': 'Отменено'
    };
    return statuses[status] || status;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('ru-RU')
}

async function logout() {
    const response = await makeRequest({
        url: "/api/auth/logout",
        method: "POST"
    })
    location.href = '/'
}

window.logout = logout