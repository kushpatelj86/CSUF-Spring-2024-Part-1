function create_user(event) {
  event.preventDefault(); // Prevent the default form submission
  
  // Get form data
  const formData = new FormData(document.querySelector('form'));
  
  // Convert form data to JSON object
  var jsonData = {};
  formData.forEach((value, key) => {
    jsonData[key] = value;
  });
  var name = document.getElementById('name').value;
  var weight = document.getElementById('weight').value;
  var height = document.getElementById('height').value;
  var age = document.getElementById('age').value;
  var allergies = document.getElementById('allergies').value;

  // Send data to backend using fetch API
  fetch('http://127.0.0.1:5000/create_user', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(jsonData),
  })
    .then(response => response.json())
    .then(data => {
      // Handle response from backend
      alert(JSON.stringify(data)); // You can display a success message or perform other actions
      var mess = document.getElementById('user');
      mess.innerHTML = JSON.stringify(data); // Clear previous content
  
    })
    .catch(error => {
      console.error('Error:', error);
    });

   





  document.getElementById('name').value = '';
  document.getElementById('age').value = '';
  document.getElementById('weight').value = '';
  document.getElementById('height').value = '';
  document.getElementById('allergies').value = 'none';
}




function get_user(event) {

  event.preventDefault(); // Prevent the default form submission


fetch('http://127.0.0.1:5000/get_users')
.then(response => response.json())
.then(users => {
  // Assuming you have a div with id 'userList' to display the users
  var userListDiv = document.getElementById('user');
  userListDiv.innerHTML = ''; // Clear previous content
  var name = document.getElementById('name').value; // Get the search input from the form
  var foundUser = users.find(user => user.NAME === name); // Find the user with the matching name
  var count = 1;
  users.forEach((user,index) => {
    if(index === (users.length - 1))
    {
      var userItem = document.createElement('div');
      userItem.textContent = `CWID: ${user[0]}, Name: ${user[1]}, Weight: ${user[2]}, Height: ${user[3]}, Age: ${user[4]}, Allergies: ${user[5]} , length:${users.length}, count: ${index}`
      userListDiv.appendChild(userItem);
    }
  });



})
.catch(error => {
  console.error('Error:', error);
  mess.innerHTML = 'Error: ' + error.message;
});



}
