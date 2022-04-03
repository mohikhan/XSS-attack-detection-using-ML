
function submitForm() {

  const name = document.getElementById('NameOnCard').value;
  const address = document.getElementById('Address').value;
  const occupation = document.getElementById('Occupation').value;
  const remarks = document.getElementById('Remarks').value;

  fetch('http://localhost:8500/checkXSS', 
    {method:'post', 
     body: JSON.stringify({
        username:name,
        address:address,
        occupation:occupation,
        remarks:remarks
     }),
     headers: {
        "Content-type": "application/json; charset=UTF-8"
     }
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error =>{
      console.log(error);
    });

  console.log('Data sent to server successfully');
//   e.preventDefault();
}