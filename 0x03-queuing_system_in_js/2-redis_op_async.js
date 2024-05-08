
import redis from 'redis'
import { promisify } from 'util'

const client = redis.createClient();

// Event listeners for Redis client

redis.on('connect', () => {
    console.log('Redis client connected to the server')
});
redis.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

const getAsync = promisify(client.get).bind(client)
// Function to display the value of a school

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(`value for ${schoolName}: ${value}`);
    }
    catch(err) {
            console.log(err);
    } 
    }

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco')