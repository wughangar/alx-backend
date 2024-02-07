import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

async function setNewSchool(schoolName, value) {
    await setAsync(schoolName, value);
    console.log(`Value ${value} set for key ${schoolName}`);
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(`Value for ${schoolName}: ${value}`);
    } catch (error) {
        console.error(`Error getting value for ${schoolName}: ${error}`);
    }
}
