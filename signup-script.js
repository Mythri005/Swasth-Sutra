document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const fullName = document.getElementById('full-name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    // Check if password and confirm password match
    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }

    // Check if the form fields are filled
    if (fullName === '' || email === '' || password === '') {
        alert('Please fill out all fields.');
        return;
    }

    // Create the user object
    const user = {
        fullName,
        email,
        password,
        confirmPassword
    };

    // Send the data to the backend
    fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
    })
    .then(response => {
        if (!response.ok) {
            // If response status is not OK, log the response status and text for debugging
            console.error('Error response from server:', response.status, response.statusText);
            return response.json(); // Read the response as JSON for error message
        }
        return response.json(); // If OK, parse the response as JSON
    })
    .then(data => {
        if (data.message) {
            // If the response has a message, redirect to login page
            window.location.href = "login.html"; // Redirect to login page
        } else {
            // If there's an error, show the error message
            alert(data.error || 'An unexpected error occurred.');
        }
    })
    .catch(err => {
        // Log the error to the console for debugging
        console.error('Request failed:', err);
        alert('Something went wrong! Please check the console for more details.');
    });
});
