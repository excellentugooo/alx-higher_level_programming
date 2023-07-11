#include "lists.h"

/**
 * insert_node - Inserts a number
 * @head: A pointer the head
 * @number: number to insert.
 *
 * Return: If the function fails - NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);
	insert->n = number;

	if (node == NULL || node->n >= number)
	{
		insert->next = node;
		*head = insert;
		return (insert);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	insert->next = node->next;
	node->next = insert;

	return (insert);
}

