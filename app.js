document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("review-form");
    const message = document.getElementById("message");
    let selectedRating = 0;

    // Handle star rating selection
    const stars = document.querySelectorAll(".star");
    stars.forEach(star => {
        star.addEventListener("click", function () {
            selectedRating = this.getAttribute("data-value"); // Get selected star value

            // Highlight all previous stars up to the selected one
            stars.forEach(s => {
                if (s.getAttribute("data-value") <= selectedRating) {
                    s.classList.add("selected");
                } else {
                    s.classList.remove("selected");
                }
            });
        });
    });

    // Handle form submission
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const name = document.getElementById("name").value;
        const review = document.getElementById("review").value;

        if (!selectedRating) {
            alert("Please select a rating!");
            return;
        }

        // Send review data to backend
        fetch("http://127.0.0.1:5000/submit-review", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, review, rating: selectedRating })
        })
        .then(response => response.json())
        .then(data => {
            message.textContent = data.message; // Show success message
            form.reset(); // Clear form
            selectedRating = 0; // Reset rating
            stars.forEach(s => s.classList.remove("selected")); // Remove star highlights
        })
        .catch(error => console.error("Error:", error));
    });
});
