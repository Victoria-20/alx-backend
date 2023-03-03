const express = require('express')
import redis from 'redis';


const client = redis.createClient({
    host: 'localhost',
    port: 6379
})

client.on('connect', () => {
    console.log("Redis client connected to the server");
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});


const listProducts = [
    {
      id: 1,
      name: 'Suitcase 250',
      price: 50,
      stock: 4
    },
    {
      id: 2,
      name: 'Suitcase 450',
      price: 100,
      stock: 10
    },
    {
      id: 3,
      name: 'Suitcase 650',
      price: 350,
      stock: 2
    },
    {
      id: 4,
      name: 'Suitcase 1050',
      price: 550,
      stock: 5
    }
];

function getItemById(id){
    for (let i = 0; i < listProducts.length; i++) {
        if (listProducts[i].id === id) {
          return listProducts[i];
        }
      }
      return null;

}

const app = express();
const port = 1245;

app.get('list_products', (req, res) => {

})

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
