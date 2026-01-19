const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const edad = document.getElementById("edad");
const btnEnviar = document.getElementById("btnEnviar");

const formulario = document.getElementById("formulario");

// Expresión regular para correo
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Validaciones
function validarNombre() {
    if (nombre.value.length >= 3) {
        setValido(nombre, "errorNombre");
        return true;
    } else {
        setInvalido(nombre, "errorNombre", "Mínimo 3 caracteres");
        return false;
    }
}

function validarCorreo() {
    if (emailRegex.test(correo.value)) {
        setValido(correo, "errorCorreo");
        return true;
    } else {
        setInvalido(correo, "errorCorreo", "Correo no válido");
        return false;
    }
}

function validarPassword() {
    const regex = /^(?=.*[0-9])(?=.*[!@#$%^&*])/;
    if (password.value.length >= 8 && regex.test(password.value)) {
        setValido(password, "errorPassword");
        return true;
    } else {
        setInvalido(
            password,
            "errorPassword",
            "Mínimo 8 caracteres, un número y un carácter especial"
        );
        return false;
    }
}

function validarConfirmPassword() {
    if (confirmPassword.value === password.value && confirmPassword.value !== "") {
        setValido(confirmPassword, "errorConfirmPassword");
        return true;
    } else {
        setInvalido(confirmPassword, "errorConfirmPassword", "No coinciden");
        return false;
    }
}

function validarEdad() {
    if (edad.value >= 18) {
        setValido(edad, "errorEdad");
        return true;
    } else {
        setInvalido(edad, "errorEdad", "Debe ser mayor o igual a 18");
        return false;
    }
}

function setValido(input, errorId) {
    input.classList.add("valido");
    input.classList.remove("invalido");
    document.getElementById(errorId).textContent = "";
}

function setInvalido(input, errorId, mensaje) {
    input.classList.add("invalido");
    input.classList.remove("valido");
    document.getElementById(errorId).textContent = mensaje;
}

function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmPassword() &&
        validarEdad()
    ) {
        btnEnviar.disabled = false;
    } else {
        btnEnviar.disabled = true;
    }
}

// Eventos en tiempo real
nombre.addEventListener("input", validarFormulario);
correo.addEventListener("input", validarFormulario);
password.addEventListener("input", validarFormulario);
confirmPassword.addEventListener("input", validarFormulario);
edad.addEventListener("input", validarFormulario);

// Envío del formulario
formulario.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("✅ Formulario validado correctamente");
});
