function sendWeeklyWorkouts(event) {
  event.preventDefault(); // Prevent form submission

  // Get the form element
  const form = document.getElementById('weeklyWorkoutForm');

  // Collect selected workouts from checkboxes
  const selectedWorkouts = {};
  const checkboxes = form.querySelectorAll('input[type="checkbox"]:checked');
  checkboxes.forEach((checkbox) => {
    const day = checkbox.name;
    const workout = checkbox.value;
    if (!(day in selectedWorkouts)) {
      selectedWorkouts[day] = [];
    }
    selectedWorkouts[day].push(workout);
  });
  alert(JSON.stringify(selectedWorkouts))

  // Send data to backend using fetch
  fetch('http://127.0.0.1:5000/send_workouts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(selectedWorkouts),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      alert(JSON.stringify(data));
      var mess = document.getElementById('workouts');
      mess.innerHTML = JSON.stringify(data); // Clear previous content


      // Optionally, update UI or show a success message
    })
    .catch((error) => {
      alert('Error sending workouts:', error);
      // Optionally, show an error message to the user
    });
}
