// Arreglo de productos
const productos = [
    {
        nombre: "Laptop",
        precio: 850,
        descripcion: "Laptop para uso académico"
    },
    {
        nombre: "Mouse",
        precio: 15,
        descripcion: "Mouse inalámbrico"
    },
    {
        nombre: "Teclado",
        precio: 25,
        descripcion: "Teclado mecánico"
    }
];

// Referencias al DOM
const listaProductos = document.getElementById("lista-productos");
const botonAgregar = document.getElementById("btn-agregar");

// Función para mostrar los productos
function renderizarProductos() {
    listaProductos.innerHTML = "";

    productos.forEach(producto => {
        const li = document.createElement("li");
        li.innerHTML = `
            <strong>${producto.nombre}</strong><br>
            Precio: $${producto.precio}<br>
            ${producto.descripcion}
        `;
        listaProductos.appendChild(li);
    });
}

// Mostrar productos al cargar la página
renderizarProductos();

// Agregar nuevo producto
botonAgregar.addEventListener("click", () => {
    const nombre = document.getElementById("nombre").value;
    const precio = document.getElementById("precio").value;
    const descripcion = document.getElementById("descripcion").value;

    if (nombre === "" || precio === "" || descripcion === "") {
        alert("Completa todos los campos");
        return;
    }

    const nuevoProducto = {
        nombre: nombre,
        precio: precio,
        descripcion: descripcion
    };

    productos.push(nuevoProducto);
    renderizarProductos();

    // Limpiar campos
    document.getElementById("nombre").value = "";
    document.getElementById("precio").value = "";
    document.getElementById("descripcion").value = "";
});
