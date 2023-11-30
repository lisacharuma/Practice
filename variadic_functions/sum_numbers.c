#include <stdio.h>
#include <stdarg.h>

/**
 * sum_numbers - a function that sums up its args
 * @n: number of args
 * Return: sum of args
 */
int sum_numbers(int n, ...)
{
	int sum = 0, i;

	if (n == 0)
		return 0;
	
	/*ptr to arg list*/
	va_list args;
	va_start(args, n); /*initializing arg list*/

	/*accessing each arg in arg list*/
	for (i = 0; i < n; i++)
		sum += va_arg(args, int);/*adding each arg to sum*/
	va_end(args);
	return sum;
}

/**
 * main - entry point
 * Return - 0
 */
int main(void)
{
	int total;

	total = sum_numbers(2, 14, 38);
	printf("The sum of the numbers is %d\n", total);
	total = sum_numbers(5, 10, 30, 44, 18, 45);
	printf("This time sum is %d\n", total);
	return 0;
}
