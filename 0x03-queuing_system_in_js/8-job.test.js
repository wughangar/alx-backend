import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient() }, testMode: true });
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  test('should throw an error if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('not an array', queue);
    }).toThrow('Jobs is not an array');
  });

  test('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '9876543210', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).toBe(2);
  });

  test('should log messages when jobs are created, completed, failed, and making progress', () => {
    const consoleLogSpy = jest.spyOn(console, 'log').mockImplementation(() => {});

    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '9876543210', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringMatching(/^Notification job created:/));
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringMatching(/^Notification job \d+ completed/));
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringMatching(/^Notification job \d+ failed:/));
    expect(consoleLogSpy).toHaveBeenCalledWith(expect.stringMatching(/^Notification job \d+ \d+% complete/));

    consoleLogSpy.mockRestore();
  });
});
