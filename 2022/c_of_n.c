#include <math.h>
#include <stdio.h>

void main() {
	int n;

	scanf("%d", &n);

	int r = (int)sqrt(n);
	int count = 0;

	for (int a = 0; a < r; a++) {
		for (int b = 0; b < r; b++) {
			if (a * a + b * b < n) {
				count++;
			}
		}
	}

	printf("%d", count);
}
