import kue from 'kue';

const queue = kue.createQueue({concurrency: 2});

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    
    if (blacklistedNumbers.includes(phoneNumber)) {
      const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
      done(error);
    } else {
      // Track the progress to 50%
      job.progress(50, 100);
      

      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

      done();
    }
  }
  
  // Process jobs in the 'push_notification_code_2' queue
  queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;

    sendNotification(phoneNumber, message, job, done);
  });
