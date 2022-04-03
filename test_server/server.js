const express = require('express');
const cors = require('cors');

const app = express();

app.use(express.json({type: 'application/json'}));

// use cors for allowing cross origin requests...
app.use(cors());

// check whether given form fields are safe to store....
app.post('/checkXSS', async (req,res) => {
    // const name = req.body.username;
    // const userAddress = req.body.address;
    // const occupation = req.body.occupation;

    console.log(req.body.username);
    // console.log('User name string =  ', name);
    // console.log('User Address string = ', userAddress);
    // consol.log('User designation string = ', occupation);
    
    // TODO: add call to ML model for performing 
    // xss attack detection
    res.status(200).send('success');
});

// listen server at the specified port....
app.listen(8500, () => {
  console.log('Express server listening on 8500');
});