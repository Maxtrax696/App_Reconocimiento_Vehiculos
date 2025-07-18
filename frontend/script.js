const form = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");

const resultContainer = document.getElementById("resultContainer");
const marca = document.getElementById("marca");
const modelo = document.getElementById("modelo");
const anio = document.getElementById("anio");
const precio = document.getElementById("precio");
const resena = document.getElementById("resena");

imageInput.addEventListener("change", () => {
  const file = imageInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      preview.src = e.target.result;
      preview.style.display = "block";
    };
    reader.readAsDataURL(file);
  }
});

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const file = imageInput.files[0];
  if (!file) return alert("Selecciona una imagen primero.");

  const formData = new FormData();
  formData.append("file", file);

  // 🔒 Bloquear botón y mostrar carga
  const submitButton = form.querySelector("button");
  submitButton.disabled = true;
  submitButton.textContent = "Analizando...";
  document.getElementById("loadingSpinner").classList.remove("d-none");
  resultContainer.classList.add("d-none");

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Estado HTTP ${response.status}`);
    }

    const data = await response.json();

    if (data.success) {
      const v = data.data;
      marca.textContent = v.marca;
      modelo.textContent = v.modelo;
      anio.textContent = v.año;
      precio.textContent = v.precio;
      resena.textContent = v.reseña;

      const recorte = document.getElementById("recorte");
      recorte.src = v.imagen;
      recorte.style.display = "block";

      resultContainer.classList.remove("d-none");

      // ✅ Guardar en historial localStorage
      const historial = JSON.parse(localStorage.getItem("historialVehiculos")) || [];
      historial.unshift({
        fecha: new Date().toLocaleString(),
        marca: v.marca,
        modelo: v.modelo,
        año: v.año,
        precio: v.precio,
        reseña: v.reseña,
        imagen: v.imagen,
      });
      localStorage.setItem("historialVehiculos", JSON.stringify(historial.slice(0, 10)));
    } else {
      alert("No se pudo analizar la imagen.");
    }
  } catch (err) {
    console.error(err);
    alert("Error al conectarse con el servidor.");
  }

  // 🔓 Restaurar botón y ocultar spinner
  submitButton.disabled = false;
  submitButton.textContent = "Analizar imagen";
  document.getElementById("loadingSpinner").classList.add("d-none");
});
