document.addEventListener('DOMContentLoaded', function () {
    const countdown = document.getElementById('countdown');
    const eventDate = new Date('2024-08-15T00:00:00'); // Fecha del evento

    function updateCountdown() {
        const now = new Date();
        const diff = eventDate - now;
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((diff % (1000 * 60)) / 1000);
        countdown.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        if (diff < 0) {
            clearInterval(interval);
            countdown.innerHTML = '¡El evento ha comenzado!';
        }
    }
    const interval = setInterval(updateCountdown, 1000);

    const form = document.getElementById('attendance-form');
    const passInfo = document.getElementById('pass-info');
    const step1 = document.getElementById('step1');
    const step2 = document.getElementById('step2');
    const checkInvitesButton = document.getElementById('check-invites');

    checkInvitesButton.addEventListener('click', async () => {
        const inputName = document.getElementById('name');
        const name = inputName.value.trim();
        if (name === '') {
            alert('Por favor, ingrese su nombre.');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:5000/verificar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ nombre: name })
            });

            const data = await response.json();

            if (data.error) {
                alert(data.error);
                return;
            }

            passInfo.innerHTML = `Tienes ${data.cantidad_invitados} pases.`;
            step1.style.display = 'none';
            step2.style.display = 'block';
        } catch (error) {
            console.log(error);
        }
    });

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const name = document.getElementById('name').value.trim();
        const attend = document.getElementById('attend').value;
        const cantidadInvitados = passInfo.innerText.split(' ')[1];

        if (!name || !attend || !cantidadInvitados) {
            alert('Por favor, completa todos los campos.');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:5000/confirmar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    nombre: name,
                    cantidad_invitados: cantidadInvitados,
                    asistencia: attend
                })
            });

            const data = await response.json();

            if (data.error) {
                alert(data.error);
            } else {
                alert(`Gracias por confirmar tu asistencia, ${name}. Asistirás: ${attend}`);
                form.reset();
                step2.style.display = 'none';
                step1.style.display = 'block';
                passInfo.innerHTML = '';
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
