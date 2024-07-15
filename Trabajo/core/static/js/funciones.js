document.addEventListener("DOMContentLoaded", function() {
    // Función para obtener los servicios y mostrarlos en la página
    function obtenerServicios() {
        fetch('http://localhost:3300/servicios')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Obtenemos el elemento donde queremos mostrar los servicios
                const listaServicios = document.getElementById('lista-servicios');

                // Limpiamos el contenido actual del elemento
                listaServicios.innerHTML = '';

                // Iteramos sobre los servicios y creamos el HTML correspondiente
                data.forEach(servicio => {
                    // Creamos un nuevo elemento <div> para el servicio
                    const servicioDiv = document.createElement('div');
                    // Añadimos el nombre y la descripción del servicio como elementos <h2> y <p>
                    servicioDiv.innerHTML = `<h2>${servicio.nombre}</h2><p>${servicio.descripcion}</p>`;
                    // Añadimos el nuevo elemento <div> al contenedor de servicios
                    listaServicios.appendChild(servicioDiv);
                });
            })
            .catch(error => {
                console.error('Se ha producido un error:', error);
            });
    }

    // Llamamos a la función para obtener y mostrar los servicios al cargar la página
    obtenerServicios();
});







