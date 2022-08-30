const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();

app.use(express.json({type: 'application/json'}));

// use cors for allowing cross origin requests...
app.use(cors());

// check whether given form fields are safe to store....
app.post('/checkXSS', async (req,res) => {
  
    const name = req.body.username;
    const address = req.body.address;
    const occupation = req.body.occupation;
    const remarks = req.body.remarks;

    console.log(name);
    console.log(address);
    console.log(occupation);
    console.log(remarks);
    
    // call to Flask API for checking xss attack.....
    let response = await axios.post('http://localhost:5000/predict', {
        name:name,
        address:address,
        occupation:occupation,
        remarks:remarks
    });

    console.log(response.data);

    if(response.data == 0){
      console.log("Form data is safe");
    }
    else {
      console.log("Form data contains malicious XSS script");
    }

    res.status(200).send('success');
});

// listen server at the specified port....
app.listen(8500, () => {
  console.log('Express server listening on 8500');
});