document.addEventListener('DOMContentLoaded', function() {
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
            modal.addEventListener('click', function(e) {
                if (e.target === this) closeAllModals();
            });
        });

        // Закрытие по кнопке "Отмена"
        document.querySelectorAll('.close-modal-btn').forEach(btn => {
            btn.addEventListener('click', closeAllModals);
        });

        // Обработчики форм
        document.getElementById('ticketForm')?.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Заявка успешно создана!');
            this.reset();
            closeAllModals();
        });

        document.getElementById('reportForm')?.addEventListener('submit', function(e) {
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
        const mockTickets = [
            { id: 1254, subject: 'Ремонт сервера Dell', status: 'active', date: '15.05.2024' },
            { id: 1253, subject: 'Настройка 1С', status: 'completed', date: '14.05.2024' },
            { id: 1252, subject: 'Замена HDD на рабочей станции', status: 'active', date: '13.05.2024' }
        ];

        const ticketsList = document.querySelector('#myTicketsModal .tickets-list');
        if (!ticketsList) return;

        ticketsList.innerHTML = mockTickets.map(ticket => `
            <div class="ticket-item">
                <div class="ticket-info">
                    <h3>#${ticket.id} - ${ticket.subject}</h3>
                    <div class="ticket-meta">
                        <span>${ticket.date}</span>
                        <span class="status ${ticket.status === 'active' ? 'in-progress' : 'completed'}">
                            ${ticket.status === 'active' ? 'В работе' : 'Завершено'}
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
        newTicketBtn.addEventListener('click', function(e) {
            e.preventDefault();
            openModal(modals.newTicket);
        });
    }

    if (reportBtn) {
        reportBtn.addEventListener('click', function(e) {
            e.preventDefault();
            openModal(modals.report);
        });
    }

    if (myTicketsBtn) {
        myTicketsBtn.addEventListener('click', function(e) {
            e.preventDefault();
            openModal(modals.myTickets);
        });
    }

    // Инициализация
    initModals();
});

document.getElementById('escape').addEventListener('change', function() {
    if(this.value === 'poka') {
        // Здесь код для выхода из системы
        window.location.href = '/logout'; // Пример перенаправления
    }
});