import redis from 'redis';

const publisher = redis.createClient();

publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

publisher.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send '${message}'`);
        publisher.publish('holberton school channel', message);
    }, time);
}
