#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <stdint.h>

uint64_t count;
pthread_mutex_t lock;
uint64_t r;
uint64_t n;

void *counter(void *vargp);

int main() 
{
	scanf("%d", &n);

	r = ceil(sqrt(n));
	count = 0;
	
	pthread_t t1, t2, t3, t4;

	if (pthread_mutex_init(&lock, NULL) != 0) {
		printf("Mutex initialization failed.\n");
		return 1;
	}

	uint64_t bounds1[] = {0l, r / 4l};
	uint64_t bounds2[] = {r / 4l, r / 2l};
	uint64_t bounds3[] = {r / 2l, r / 4l * 3l};
	uint64_t bounds4[] = {r / 4l * 3l, r};

	pthread_create(&t1, NULL, counter, bounds1);
	pthread_create(&t2, NULL, counter, bounds2);
	pthread_create(&t3, NULL, counter, bounds3);
	pthread_create(&t4, NULL, counter, bounds4);

	pthread_join(t1, NULL);
	pthread_join(t2, NULL);
	pthread_join(t3, NULL);
	pthread_join(t4, NULL);

	printf("%d\n", count);
}

void *counter(void *vargp) 
{
	uint64_t *args = (uint64_t *) vargp;
	uint64_t loc_count = 0;

	for (uint64_t a = args[0]; a < args[1]; a++) {
		for (uint64_t b = 0; b < r; b++) {
			if (a * a + b * b < n) {
				loc_count++;
			}
		}
	}
	pthread_mutex_lock(&lock);
	count += loc_count;	
	pthread_mutex_unlock(&lock);
}
