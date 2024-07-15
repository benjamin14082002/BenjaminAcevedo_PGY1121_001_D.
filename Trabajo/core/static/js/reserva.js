document.addEventListener('DOMContentLoaded', function() {
  var form = document.getElementById('dateForm');
  form.addEventListener('submit', function(event) {
      event.preventDefault();  // Evitar el envío del formulario por defecto

      var fecha = document.getElementById('fecha').value;
      var hora = document.getElementById('hora').value;

      // Validar si se ha seleccionado una fecha y hora
      if (!fecha || !hora) {
          alert("Por favor, seleccione una fecha y una hora.");
          return;
      }

      var fechaActual = new Date();
      var seleccionFecha = new Date(fecha + 'T' + hora);

      if (seleccionFecha < fechaActual) {
          alert("La fecha y hora seleccionadas deben ser en el futuro.");
          return;
      }

      // Hacer la petición POST para guardar la reserva en el servidor
      var url = '/reservar/';  // Reemplaza con la URL correcta de tu backend
      var data = {
          fecha: fecha,
          hora: hora
      };

      fetch(url, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie('csrftoken')  // Asegúrate de obtener correctamente el token CSRF si es necesario
          },
          body: JSON.stringify(data)
      })
      .then(response => {
          if (response.ok) {
              return response.json();
          }
          throw new Error('Error en la solicitud');
      })
      .then(data => {
          console.log(data);  // Maneja la respuesta del servidor aquí
          // Por ejemplo, mostrar un mensaje de éxito o actualizar la UI
          alert("Reserva confirmada para el " + fecha + " a las " + hora);
          
          // Guardar los datos en localStorage
          let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
          carrito.push({ fecha: fecha, hora: hora });
          localStorage.setItem('carrito', JSON.stringify(carrito));

          // Aquí puedes agregar lógica adicional según sea necesario
      })
      .catch(error => {
          console.error('Error:', error);
          alert("Hubo un error al procesar la reserva.");
      });
  });

  // Función auxiliar para obtener el token CSRF
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = cookies[i].trim();
              // Buscar el token CSRF por su nombre
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
});
