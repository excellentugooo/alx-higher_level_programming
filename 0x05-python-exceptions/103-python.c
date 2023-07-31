/*
 * File: 103-python.c
 * Auth: Type Your Name Here
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t list_size, list_alloc, i;
    const char *element_type;
    PyListObject *list_var = (PyListObject *)p;
    PyVarObject *list_obj = (PyVarObject *)p;

    list_size = list_obj->ob_size;
    list_alloc = list_var->allocated;

    fflush(stdout);

    printf("[*] Python list info\n");
    if (strcmp(p->ob_type->tp_name, "list") != 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", list_alloc);

    for (i = 0; i < list_size; i++)
    {
        element_type = list_var->ob_item[i]->ob_type->tp_name;
        printf("Element %ld: %s\n", i, element_type);
        if (strcmp(element_type, "bytes") == 0)
            print_python_bytes(list_var->ob_item[i]);
        else if (strcmp(element_type, "float") == 0)
            print_python_float(list_var->ob_item[i]);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t bytes_size, i;
    PyBytesObject *bytes_var = (PyBytesObject *)p;

    fflush(stdout);

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_size = ((PyVarObject *)p)->ob_size;
    printf("  size: %ld\n", bytes_size);
    printf("  trying string: %s\n", bytes_var->ob_sval);

    if (bytes_size >= 10)
        bytes_size = 10;

    printf("  first %ld bytes: ", bytes_size);
    for (i = 0; i < bytes_size; i++)
    {
        printf("%02hhx", bytes_var->ob_sval[i]);
        if (i == (bytes_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
    char *buff = NULL;

    PyFloatObject *float_obj = (PyFloatObject *)p;

    fflush(stdout);

    printf("[.] float object info\n");
    if (strcmp(p->ob_type->tp_name, "float") != 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
                                 Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buff);
    PyMem_Free(buff);
}

