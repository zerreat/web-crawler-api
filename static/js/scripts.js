
function showLoading(event) {
    event.preventDefault(); 

    const formData = new FormData(event.target);
    const root_url = formData.get('root_url');
    const depth = formData.get('depth');

    document.getElementById('loading').style.display = 'block';

    fetch('/crawl', {
        method: 'POST',
        body: new URLSearchParams(formData), 
    })
    .then(response => response.text()) 
    .then(html => {
        setTimeout(() => {
            document.body.innerHTML = html;

            document.getElementById('loading').style.display = 'none';
        }, 1000); 
    })
    .catch(error => {
        console.error('Error during fetch:', error);
        document.getElementById('loading').style.display = 'none';

        alert("An error occurred. Please try again.");
    });
}

function resetPage() {
    document.getElementById('loading').style.display = 'none';
}

window.onload = resetPage;
