#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: address of linked list
 * @number: the data to be inserted
 *
 * Return: the adress of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *list;

	if (*head == NULL)
	{
		printf("%d\n", number);
		return (NULL);
	}
	list = *head;
	temp = malloc(sizeof(listint_t));
	temp->n = number;
	temp->next = NULL;

	while (list->n < number)
	{
		if (list->next->n < number && list->next->next == NULL)
		{
			list = list->next;
			list->next = temp;
			return (temp);
		}
		if (list->next->n >= number)
		{
			temp->next = list->next;
			list->next = temp;
			return (temp);
		}
		list = list->next;
	}
	temp->next = list;
	*head = temp;

	return (temp);
}
