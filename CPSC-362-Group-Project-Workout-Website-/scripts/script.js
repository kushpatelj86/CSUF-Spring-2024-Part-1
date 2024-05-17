
function calcBMI(){
    let weight = document.getElementById("weight").value;
    let height = document.getElementById("height").value;


    let bmi = Math.round(((weight / (height * height) * 703 )) * 10) / 10;

    document.getElementById("BMI-Heading").innerHTML = "Your BMI is: ";
    
    
    if(isNaN(weight) || isNaN(height) || weight == null || height == null || weight == "" || height == "")
    {
        
        
        document.getElementById("BMI-Heading").innerHTML = "Please Enter Both Height and Weight ";
        document.getElementById("BMI").innerHTML = "";
        document.getElementById("Health-Status").innerHTML = "Unable to calculate to BMI";


        
    }
    else
    {
        document.getElementById("BMI-Heading").innerHTML = "Your BMI is: ";
        document.getElementById("BMI").innerHTML = bmi;

            if(bmi < 18.5)
            {
                document.getElementById("Health-Status").innerHTML = "You are underweight. Consider nutritional consultation with us to assess your diet";
            }
            else if (bmi >= 18.5 && bmi <= 24.9)
            {
                document.getElementById("Health-Status").innerHTML = "You are a healthy weight. Mantain your current diet and excercise routine."; 
            }
            else if (bmi >= 25 && bmi <= 29.9)
            {
                document.getElementById("Health-Status").innerHTML = "You are overweight. Consider moderate excercise and consulting us to review your diet.";
            }
            else if (bmi >= 30)
            {
                document.getElementById("Health-Status").innerHTML = "You have Obesity. It's important to seek consulting from us to develop a personalized diet and excercise plan.";
            }
            else
            {
                
            }
    }

    
}

function reload()
{
    window.location.reload();
}


  
  
  













































  function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }


  function generatePlan(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    document.getElementById('plan').innerHTML = `Loading...`;

    fetch('http://127.0.0.1:3456/users')
    .then(response => response.json() )
    .then(data => {
        document.getElementById('plan').innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(err => {
        document.getElementById('plan').innerHTML = `Error fetching data: ${err.message}`;
    });
}







  /*$.ajax({
      type: 'POST',
      url: '/create_user', // Assuming this is the correct endpoint on your backend
      contentType: 'application/json', // Make sure this line is present and correctly set
      data: JSON.stringify(formData),
      success: function(response) {
          // Update message container with success message from server
          $('#message').text(response.message);
        
      },
      error: function(xhr, status, error) {
          // Update message container with error message
          $('#message').text('Error creating user: ' + error);
      }
  });*/


/*fetch('/create_user', {
  method: 'POST',  // Ensure this matches the expected method in your Flask route
  headers: {
      'Content-Type': 'application/json',
  },
  body: JSON.stringify(formData),
})
.then(response => response.json())
.then(data => {
  // Handle response data
  alert('User created successfully, '+ data);
})
.catch(error => {
  alert('Error creating user: ' + error)
});*/


























function navigate(event)
{
  event.preventDefault(); // Prevent the form from submitting normally

  // Get the values of the username and password inputs
  var username = document.getElementById("username").value.trim();
  var password = document.getElementById("password").value.trim();

  // Check if both inputs are not empty
  if (username !== "" && password !== "") {
      // Navigate to another page (replace 'target_page.html' with the actual page URL)
      window.location.href = 'menupage.html';
  } else {
      alert("Please enter both username and password.");
  }
  
 
}

