document.addEventListener("DOMContentLoaded", function () {
    let modal = document.getElementById("revenue-modal");
    let revenueText = document.getElementById("revenue-amount");
    let revenueBtn = document.getElementById("revenue-btn");
    let closeModal = document.querySelector(".close");

    if (!modal || !revenueText || !revenueBtn || !closeModal) {
        console.error("Ошибка: Один из элементов модального окна не найден.");
        return;
    }

    revenueBtn.onclick = function () {
        revenueText.innerText = "Загрузка...";
        modal.style.display = "block";

        fetch("/orders/revenue/")
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Ошибка HTTP: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                revenueText.innerText = `₽ ${parseFloat(data.total_revenue).toLocaleString("ru-RU")}`;
            })
            .catch(error => {
                console.error("Ошибка загрузки выручки:", error);
                revenueText.innerText = "Ошибка загрузки!";
            });
    };

    closeModal.onclick = function () {
        modal.style.display = "none";
    };

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
});
