import redis from 'redis';

const publisher = redis.createClient();

publisher.once('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

async function publishMessage(message, time) {
  const total = `About to send ${message}`;
  await new Promise((resolve) => setTimeout(resolve, time));
  publisher.publish('holberton school channel', message);
  console.log(total);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
