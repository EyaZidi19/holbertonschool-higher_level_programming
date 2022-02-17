#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome -fun to validate if a linked list is a palindrome
 * @head: the address to linked list
 * Return: 1 if is palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int sizeList = 0;
	int i = 0;
	int f = 0;
	int middle;
	int *newArray;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (temp->next)
	{
		sizeList++;
		temp = temp->next;
	}
	newArray = malloc(sizeof(int) * sizeList);
	temp = *head;
	while (temp)
	{
		newArray[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i--;
	middle = i / 2;
	while (f <= middle)
	{
		if (newArray[f] != newArray[i])
		{
			free(newArray);
			return (0);
		}
		i--;
		f++;
	}
	free(newArray);
	return (1);
}
