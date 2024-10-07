// Script para manejar el modal
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('modal-image');
    const captionText = document.getElementById('caption');
    const closeBtn = document.getElementsByClassName('close')[0];

    document.querySelectorAll('.gallery-item').forEach(item => {
        item.addEventListener('click', function () {
            modal.style.display = "block";
            modalImg.src = this.dataset.image;
            captionText.innerHTML = this.querySelector('img').alt;
        });
    });

    // Cerrar el modal
    closeBtn.onclick = function() {
        modal.style.display = "none";
    };

    // Cerrar el modal al hacer clic fuera de la imagen
    modal.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
});
