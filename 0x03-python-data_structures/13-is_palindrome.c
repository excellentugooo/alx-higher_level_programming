#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - Reverses a singly-linked list
 * @head: A pointer to the starting node
 *
 * Return: A pointer to the head
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *nod = *head, *next, *previous = NULL;

	while (nod)
	{
		next = nod->next;
		nod->next = previous;
		previous = nod;
		nod = next;
	}

	*head = previous;
	return (*head);
}

/**
 * is_palindrome - Checks for a palindrome.
 * @head: A pointer to the head
 *
 * Return: If  not palindrome - 0.
 *         If palindrome - 1.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *revy, *middle;
	size_t size = 0, x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (x = 0; x < (size / 2) - 1; x++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	revy = reverse_listint(&temp);
	middle = revy;

	temp = *head;
	while (revy)
	{
		if (temp->n != revy->n)
			return (0);
		temp = temp->next;
		revy = revy->next;
	}
	reverse_listint(&middle);

	return (1);
}
