//codigo para la barra de scooll
const barra = document.getElementById("barra");

function actualizarBarra() {
    const altura = document.documentElement.scrollHeight - window.innerHeight;
    let progreso = 0;
    if (altura > 0) {
        progreso = (window.scrollY / altura) * 100;
    }
    barra.style.width = progreso + "%"; // la transición CSS hace que sea suave
}

window.addEventListener("scroll", actualizarBarra);
window.addEventListener("resize", actualizarBarra);
window.addEventListener("load", actualizarBarra);




//menu ahmburquesa 


const hamburger = document.getElementById("hamburger");
const navMenu = document.getElementById("nav-menu");
const overlay = document.getElementById("overlay");

// Función para abrir/cerrar menú
function toggleMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
    overlay.classList.toggle("active");
}

// Abrir/cerrar con hamburguesa o overlay
hamburger.addEventListener("click", toggleMenu);
overlay.addEventListener("click", toggleMenu);

// Cerrar menú al hacer clic en un enlace
navMenu.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
        // Solo cerrar si el menú está abierto
        if (navMenu.classList.contains("active")) {
            toggleMenu();
        }
    });
});

