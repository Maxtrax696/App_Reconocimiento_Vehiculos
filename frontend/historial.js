const contenedor = document.getElementById("historialContainer");
const historial = JSON.parse(localStorage.getItem("historialVehiculos")) || [];

if (historial.length === 0) {
  contenedor.innerHTML = "<p class='text-muted'>No hay búsquedas guardadas aún.</p>";
} else {
  historial.forEach((item, index) => {
    const col = document.createElement("div");
    col.className = "col-md-6 col-lg-4";

    col.innerHTML = `
      <div class="card shadow-sm" id="card-${index}">
        <img src="${item.imagen}" class="card-img-top" alt="Recorte vehículo">
        <div class="card-body">
          <h5 class="card-title">${item.marca} ${item.modelo}</h5>
          <p class="card-text">
            <strong>Año:</strong> ${item.año}<br>
            <strong>Precio:</strong> ${item.precio}<br>
            <strong>Fecha:</strong> ${item.fecha}
          </p>
          <p class="text-muted small">${item.reseña}</p>
          <button class="btn btn-sm btn-outline-success mt-2" onclick="descargarTarjeta('card-${index}', '${item.marca}_${item.modelo}.jpg')">
            💾 Descargar como imagen
          </button>
        </div>
      </div>
    `;

    contenedor.appendChild(col);
  });
}

// Función para descargar la tarjeta como imagen
function descargarTarjeta(elementId, filename) {
  const card = document.getElementById(elementId);
  const boton = card.querySelector("button");

  // Ocultar botón antes de capturar
  boton.style.visibility = "hidden";

  html2canvas(card).then((canvas) => {
    // Restaurar botón después de capturar
    boton.style.visibility = "visible";

    const link = document.createElement("a");
    link.download = filename;
    link.href = canvas.toDataURL("image/jpeg");
    link.click();
  });
}

