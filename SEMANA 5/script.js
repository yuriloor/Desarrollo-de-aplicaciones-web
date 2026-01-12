const imageUrlInput = document.getElementById("imageUrl");
const addImageBtn = document.getElementById("addImageBtn");
const deleteImageBtn = document.getElementById("deleteImageBtn");
const gallery = document.getElementById("gallery");

let selectedImage = null;

// Agregar imagen
addImageBtn.addEventListener("click", () => {
    const url = imageUrlInput.value.trim();

    if (url === "") {
        alert("Ingresa una URL válida");
        return;
    }

    const img = document.createElement("img");
    img.src = url;

    // Error si la imagen no carga
    img.onerror = () => {
        alert("La URL no es una imagen válida");
        img.remove();
    };

    // Seleccionar imagen
    img.addEventListener("click", () => {
        if (selectedImage) {
            selectedImage.classList.remove("selected");
        }
        img.classList.add("selected");
        selectedImage = img;
    });

    gallery.appendChild(img);
    imageUrlInput.value = "";
});

// Eliminar imagen seleccionada
deleteImageBtn.addEventListener("click", () => {
    if (selectedImage) {
        gallery.removeChild(selectedImage);
        selectedImage = null;
    } else {
        alert("No hay imagen seleccionada");
    }
});

// Atajo de teclado: tecla Delete
document.addEventListener("keydown", (event) => {
    if (event.key === "Delete" && selectedImage) {
        gallery.removeChild(selectedImage);
        selectedImage = null;
    }
});
