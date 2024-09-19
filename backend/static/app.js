document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('product-form');
    const productTableBody = document.querySelector('#product-table tbody');

    // Функция для обновления списка продуктов
    function fetchProducts() {
        fetch('/api/products/')
            .then(response => response.json())
            .then(data => {
                productTableBody.innerHTML = '';
                data.forEach(product => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${product.name}</td>
                        <td>${product.description}</td>
                        <td>${product.price}</td>
                    `;
                    productTableBody.appendChild(row);
                });
            })
            .catch(error => console.error('Ошибка:', error));
    }

    // Обработчик отправки формы
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = {
            name: document.getElementById('name').value,
            description: document.getElementById('description').value,
            price: document.getElementById('price').value
        };

        fetch('/api/products/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при создании продукта');
            }
            return response.json();
        })
        .then(data => {
            console.log('Продукт добавлен:', data);
            // Обновляем список продуктов после успешного добавления
            fetchProducts();
            // Очищаем форму
            form.reset();
        })
        .catch(error => console.error('Ошибка:', error));
    });

    // Первоначальная загрузка списка продуктов
    fetchProducts();
});