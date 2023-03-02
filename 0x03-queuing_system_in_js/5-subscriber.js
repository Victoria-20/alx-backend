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

// subscribe channel
client.subscribe('holberton school channel');

client.on('message', (err, msg) => {
    if (msg === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.end(true);
    }
    console.log(msg);
});
