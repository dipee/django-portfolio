document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    fetch('/contact/', {
        method: 'POST',
        body: new FormData(event.target),
    })
    .then(response => response.json())
    .then(data => {
        var toast = document.getElementById('toast');
        console.log(data.message)
        toast.innerText = data.message;
        toast.className = 'show';
        setTimeout(function(){ toast.className = toast.className.replace('show', 'hide'); }, 3000);
    });
});