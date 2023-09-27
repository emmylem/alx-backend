import redis from 'redis';

const subscriber = redis.createClient();

subscriber.once('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

subscriber.on('message', async (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    await subscriber.unsubscribe();
    await subscriber.quit();
  }
});

subscriber.subscribe('holberton school channel');
