// Import the necessary module
import redis from 'redis';

// Create a Redis client for subscribing
const subscriber = redis.createClient();

// Connect to the Redis server
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
subscriber.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Listen for messages
subscriber.on('message', (channel, message) => {
  console.log(`Received message from channel ${channel}: ${message}`);
  
  // Check if the message is KILL_SERVER
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
