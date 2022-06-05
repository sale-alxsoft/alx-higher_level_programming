#include "lists.h"
/**
 * is_palindrome - check singly list if it is a palindrome
 * @head: singly linked list
 *
 * Return: 0 if it is not, or 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list;
	listint_t *last_node;
	listint_t *temp;

	list = *head;
	last_node = *head;
	while (last_node->next != NULL)
		last_node = last_node->next;

	while (list->next != last_node->next)
	{
		temp = *head;
		if (list->n != last_node->n)
			return (0);
		while (temp->next != last_node)
		{
			temp = temp->next;
		}
		last_node = temp;
		list = list->next;
		if (list->n != last_node->n)
			return (0);
	}
	return (1);
}
