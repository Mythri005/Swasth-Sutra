let totalWaterGoal = 2000; // Example: goal is 2000 ml per day.
let currentWaterIntake = 0;
let points = 0;

// Update water percentage and background water level
function updateWaterPercentage() {
    const percentage = (currentWaterIntake / totalWaterGoal) * 100;
    const waterLevel = document.getElementById('water-level');
    const percentageDisplay = document.getElementById('percentage');
    
    // Apply the water fill based on the percentage
    waterLevel.style.height = `${percentage}%`;
    percentageDisplay.textContent = `${Math.min(percentage, 100).toFixed(0)}%`;

    // Calculate points based on water intake percentage
    points = Math.floor(percentage);
    document.getElementById('points').textContent = `Points: ${points}`;
}

// Handle adding water intake
document.getElementById('add-water').addEventListener('click', function() {
    const waterIntake = document.getElementById('water_intake').value;
    if (waterIntake && waterIntake > 0) {
        currentWaterIntake += parseFloat(waterIntake);
        if (currentWaterIntake > totalWaterGoal) {
            currentWaterIntake = totalWaterGoal; // Cap it to the goal
        }
        updateWaterPercentage();
        document.getElementById('water_intake').value = ''; // Clear input
    }
});

// Optionally, handle the Date field if needed for additional functionality
document.getElementById('date').addEventListener('change', function(e) {
    const selectedDate = e.target.value;
    console.log(`Date selected: ${selectedDate}`);
});
