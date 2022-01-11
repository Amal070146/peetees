const menuBtn = document.querySelector('.menu-icon');
const navContainer = document.querySelector('.nav-container');
const handleClick = (e) => {
    navContainer.classList.toggle("hidden");
}
menuBtn.addEventListener('click', handleClick);
