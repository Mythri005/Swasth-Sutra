window.onload = () => {
    const container = document.getElementById('meal-plan-days');
    for (let i = 1; i <= 30; i++) {
        const dayDiv = document.createElement('div');
        dayDiv.className = 'meal-day';
        dayDiv.innerHTML = `
            <h3>Day ${i}</h3>
            <ul>
                <li><input type="checkbox" onchange="checkMeals(this)"> Breakfast</li>
                <li><input type="checkbox" onchange="checkMeals(this)"> Lunch</li>
                <li><input type="checkbox" onchange="checkMeals(this)"> Dinner</li>
            </ul>
            <button onclick="markComplete(this)" disabled>Complete</button>
        `;
        container.appendChild(dayDiv);
    }
};

function checkMeals(checkbox) {
    const day = checkbox.closest('.meal-day');
    const checkboxes = day.querySelectorAll('input[type="checkbox"]');
    const button = day.querySelector('button');

    // Enable the "Complete" button if all checkboxes are checked
    button.disabled = ![...checkboxes].every(cb => cb.checked);
    
    // Update the button text to "Completed" if enabled
    button.textContent = button.disabled ? 'Complete' : 'Completed';

    // Update the progress bar
    updateProgress();
}

function updateProgress() {
    const completed = document.querySelectorAll('.meal-day button:not([disabled])').length;
    const totalDays = 30;
    const percentage = Math.round((completed / totalDays) * 100);
    document.getElementById('completion-percentage').innerText = `${percentage}% Completed`;
    document.getElementById('progress').style.width = `${percentage}%`;
}

function markComplete(button) {
    // Mark the day as completed
    button.innerText = "Completed";
    button.disabled = true;
    
    // Update the progress after marking the meal as completed
    updateProgress();
}
