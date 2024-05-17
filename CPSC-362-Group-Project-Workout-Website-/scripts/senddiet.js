

function getFoodItems(event) {

  event.preventDefault(); // Prevent form submission
  const formData = new FormData(document.querySelector('form'));
  
  // Convert form data to JSON object
  var jsonData = {};
  formData.forEach((value, key) => {
    jsonData[key] = value;
  });
  const foodGroup = document.getElementById('food_group').value;
  alert(JSON.stringify({ food_group: foodGroup }))
  fetch('http://127.0.0.1:5000/send_diet', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ food_group: foodGroup })
  })
  .then(response => response.json())
  .then(data => {
      alert(data)
      var mess = document.getElementById('diet');
      mess.innerHTML = JSON.stringify(data); // Clear previous content
  })
  .catch((error) => {
    alert(error);
    // Optionally, show an error message to the user
  });}

