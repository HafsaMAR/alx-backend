
import redis from 'redis'

const client = redis.createClient();

// Event listeners for Redis client

redis.on('connect', () => {
    console.log('Redis client connected to the server')
});
redis.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});
