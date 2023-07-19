#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes info
 *
 * @p: Python Object
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, end;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		end = 10;
	else
		end = size + 1;

	printf("  first %ld bytes:", end);

	for (i = 0; i < end; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list info
 *
 * @p: Python Object
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *lists;
	PyObject *object;

	size = ((PyVarObject *)(p))->ob_size;
	lists = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lists->allocated);

	for (i = 0; i < size; i++)
	{
		object = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
