// Import the necessary modules
import kue from 'kue';
import { createPushNotificationsJobs } from './8-job.js'; // Assuming the file is in the same directory


describe('createPushNotificationsJobs', () => {

  let queue;

  // Set up before each test
  beforeEach(() => {
    // Create a new queue in test mode
    queue = kue.createQueue({ disableSearch: true, jobEvents: false });
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  // Test case 1: Jobs is not an array
  it('throws an error if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('not an array', queue);
    }).toThrow('Jobs is not an array');
  });

  // Test case 2: Jobs array with valid job objects
  it('creates jobs in the queue', () => {
    // Define an array of job objects
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Expect two jobs to be created in the queue
    expect(queue.testMode.jobs.length).toBe(2);
  });

});
