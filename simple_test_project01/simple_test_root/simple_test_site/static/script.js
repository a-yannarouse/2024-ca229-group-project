
document.addEventListener('DOMContentLoaded', function() {
    const toggleNavButton = document.getElementById('toggleNav');
    const navMenu = document.getElementById('nav');
    
    console.log(toggleNavButton); 

    toggleNavButton.addEventListener('click', function() {
        console.log('Toggle button clicked'); 
        navMenu.classList.toggle('show');
    });
});

