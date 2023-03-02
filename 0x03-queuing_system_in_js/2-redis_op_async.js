import { redisClientFactory } from 'kue';
import * as redis from 'redis';


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


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    await client.get(schoolName, (err, value) => {
        console.log(value);
    });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
