#include <stdio.h>
#include <string.h>

typedef struct {
	int id;
	char title[40];
	float hours;
}course;

void update_course(course *class);
void display_course(course class);

int main(void)
{
	course c2; //new variable of course data type
	update_course(&c2); //call by reference
	display_course(c2); // call by value

	return(0);
}

/**
 * update_course - function that updates course by reference to new given info
 * @class: pointer to a variable of the course data type
 * Return: void
 *
 */

void update_course(course *class)
{
	class-> id = 124;
	// we use strcpy to initialize char variables
	strcpy(class -> title, "C++ Fundametals");
	class-> hours = 12.50;
}


/**
 * display_course - function that displays a given course
 * @class: variable of the course data type
 * return: void
 */

void display_course(course class)
{
	printf("%d\t %s\t %3.2f\n", class.id, class.title, class.hours);
}

