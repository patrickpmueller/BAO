#include <math.h>
#include <stdio.h>
#include <stdint.h>

void main() 
{
	uint64_t n;

	scanf("%d", &n);

	uint64_t r = ceil(sqrt(n));
	uint64_t count = 0;

	for (uint64_t a = 0; a < r; a++) {
		for (uint64_t b = 0; b < r; b++) {
			if (a * a + b * b < n) {
				count++;
			}
		}
	}

	printf("%d\n", count);
}
