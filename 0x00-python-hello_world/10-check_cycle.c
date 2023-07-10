#include "lists.h"

/**
 * check_cycle - checks for a cycle
 * @list: list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (!list)
		return (0);

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}

	return (0);
}
