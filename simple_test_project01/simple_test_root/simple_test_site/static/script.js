
document.addEventListener('DOMContentLoaded', function() {
    const toggleNavButton = document.getElementById('toggleNav');
    const navMenu = document.getElementById('nav');
    
    console.log(toggleNavButton); // Log toggleNavButton to console

    toggleNavButton.addEventListener('click', function() {
        console.log('Toggle button clicked'); // Log message when button is clicked
        navMenu.classList.toggle('show');
    });
});

