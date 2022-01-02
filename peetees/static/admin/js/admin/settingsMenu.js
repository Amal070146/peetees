const account = document.querySelector('.account-image');
const menu = document.querySelector('.settings-menu');
account.addEventListener('click', () => {
    console.log('click');
    menu.classList.toggle('hidden');
});