
import redis from 'redis'

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

// Function to display the value of a school

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.log(err);
        } else {
            console.log(`value for ${schoolName}: ${reply}`);
        }
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco')