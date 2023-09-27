import kue from 'kue';

const queue = kue.createQueue();

async function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

queue.process('push_notification_code', async (job, done) => {
  const { phoneNumber, message } = job.data;
  await sendNotification(phoneNumber, message);
  done();
});
