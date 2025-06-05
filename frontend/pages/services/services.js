document.querySelectorAll('.toggle-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const details = this.nextElementSibling;

                // Просто переключаем текущий блок
                details.classList.toggle('active');
                this.textContent = details.classList.contains('active') ? 'Свернуть' : 'Подробнее';
            });
        });
