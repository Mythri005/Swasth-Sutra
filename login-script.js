document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form from refreshing the page

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email === '' || password === '') {
        alert('Please fill out both fields.');
        return;
    }

    // Create a user object with the email and password to send to the backend
    const loginData = {
        email,
        password
    };

    // Send login data to the backend (Flask server)
    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {

            window.location.href = 'dashboard.html';  // Redirect to dashboard after successful login
        } else {
            alert(data.error);  // Show error message if login fails
        }
    })
    .catch(err => {
        console.error('Error:', err);
        alert('Something went wrong. Please try again.');
    });
});
