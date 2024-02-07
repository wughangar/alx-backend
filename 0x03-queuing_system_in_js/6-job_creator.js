import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello, this is a notification message.'
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', (jobId) => {
    console.log(`Notification job created: ${jobId}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});

job.save((error) => {
    if (error) {
        console.error('Error creating job:', error);
    } else {
        console.log('Job saved to the queue');
    }
});
