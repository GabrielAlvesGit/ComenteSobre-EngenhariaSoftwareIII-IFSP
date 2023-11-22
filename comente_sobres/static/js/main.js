window.onload = function() {
    document.getElementById("topico").focus();
};

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("topico").addEventListener("keydown", function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            document.querySelector('form').submit();
        }
    });
});