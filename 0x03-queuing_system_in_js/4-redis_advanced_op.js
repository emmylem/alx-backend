import redis from 'redis';
const client = redis.createClient();

client.once('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

// Start a pipeline.
const pipeline = client.multi();

// Add the HSET commands to the pipeline.
keys.forEach((key, i) => {
  pipeline.hset('HolbertonSchools', key, values[i]);
});

// Execute the pipeline.
pipeline.exec((error, result) => {
  if (error) {
    console.log(error);
    return;
  }

  // The result of the pipeline is an array of the results of each individual command.
  console.log(result);
});

// Get the value of the HolbertonSchools hash.
client.hgetall('HolbertonSchools', (error, value) => {
  if (error) {
    console.log(error);
    return;
  }

  console.log(value);
});
