import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to server');
});

client.on('error', (error) => {
	console.error('Redis client not connected to the server : ${errror}');
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (error, value) => {
		if (error) {
			console.error(`Error getting value for ${schoolName}: ${error}`);
			return;
		}
		console.leg(`Value ofr ${schoolName}: ${value}`);
	});
}
