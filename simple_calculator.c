#include <stdio.h>

/**
 * add - a function that adds two numbers
 * @a: firts number to add
 * @b: second number
 * Return: sum
 */

float add(float a, float b)
{
	return a + b;
}

/**
 * subtract - a function that subtracts a numbr from another
 * @a: value to subtract from
 * @b: value to subtract
 * Return: a - b
 */

float subtract(float a, float b)
{
	return a - b;
}


/**
 * mul - multiplies two numbers
 * @a: value 1
 * @b: value 2
 * Return: a*b
 */
float mul(float a, float b)
{
	return a * b;
}

/**
 * div - divides two numbers
 * @a: first num
 * @b: second num
 * Return: a / b
 */
float div(float a, float b)
{
	return a / b;
}


int main(void)
{
	int choice;
	float a, b, result;

	printf("Please enter choice: 0 for add, 1 for subtract, 2 for mul, 3 for div: \n");
	scanf("%d", &choice);

	printf("Enter two numbers: ");
	scanf("%f %f", &a, &b);

	switch (choice){
		case 0: result = add(a, b); break;
		case 1: result = subtract(a, b); break;
		case 2: result = mul(a, b); break;
		case 3: result = div(a, b); break;
	}
	printf("%f\n", result);
	return 0;
}
