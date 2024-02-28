document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    fetch('/contact/', {
        method: 'POST',
        body: new FormData(event.target),
    })
    .then(response => response.json())
    .then(data => {
        const toast = document.getElementById('toast');
        toast.innerText = data.message;
        toast.className = 'show';
        setTimeout(function(){ toast.className = toast.className.replace('show', ''); }, 3000);
    });
});