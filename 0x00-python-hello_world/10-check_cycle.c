#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if the linked list is cycle
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);
	temp = list;
	list = list->next;
	while (list != NULL)
	{
		if (list == temp)
			return (1);
		list = list->next;
	}
	return (0);
}
